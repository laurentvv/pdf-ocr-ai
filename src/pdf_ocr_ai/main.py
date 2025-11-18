"""
PDF to Markdown OCR - Main processing module

This module provides functions for converting PDF files to Markdown format
using AI-powered OCR from multiple providers.
"""
import argparse
import sys
import time
from pathlib import Path
from typing import List, Tuple

import fitz  # PyMuPDF
from tqdm import tqdm

from .providers import get_provider


def pdf_to_images(pdf_path: str, dpi: int = 300) -> List[Tuple[int, bytes]]:
    """Convert PDF pages to PNG images in memory.

    Args:
        pdf_path: Path to the input PDF file
        dpi: Resolution for image conversion (default: 300)

    Returns:
        List of tuples containing (page_number, image_bytes) for each page
    """
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=dpi)  # Higher DPI for better OCR accuracy
        img_data = pix.tobytes("png")
        images.append(
            (page_num + 1, img_data)
        )  # Page number (1-indexed) and image bytes
    doc.close()
    return images


def process_pdf_to_markdown(
    pdf_path: str, output_md_path: str, provider_type: str = "lm-studio",
    model: str = "qwen/qwen3-vl-30b", provider_url: str = None, dpi: int = 300
) -> None:
    """Main function to process PDF and generate Markdown with progress tracking.

    Args:
        pdf_path: Path to the input PDF file
        output_md_path: Path for the output Markdown file
        provider_type: AI provider to use (default: "lm-studio")
        model: Model to use with the provider (default: "qwen/qwen3-vl-30b")
        provider_url: Custom provider URL (default: None)
        dpi: Resolution for image conversion (default: 300)

    Returns:
        None (writes output to specified file)
    """
    start_time = time.perf_counter()

    # Initialize the appropriate provider
    provider = get_provider(provider_type, base_url=provider_url)

    images = pdf_to_images(pdf_path, dpi)
    total_pages = len(images)

    print(f"Starting OCR processing for {total_pages} pages...")

    with open(output_md_path, "w", encoding="utf-8") as md_file:
        md_file.write(f"# OCR Extracted Content from {Path(pdf_path).name}\n\n")

        # Initialize progress bar
        progress_bar = tqdm(
            total=total_pages, desc="Processing pages", unit="page", leave=True
        )

        for page_num, img_bytes in images:
            page_start_time = time.perf_counter()
            ocr_result = provider.ocr_image(img_bytes, model)
            page_end_time = time.perf_counter()

            # Calculate page processing time
            page_time = page_end_time - page_start_time

            md_file.write(f"## Page {page_num}\n\n")
            md_file.write(ocr_result + "\n\n---\n\n")

            # Update progress bar with page processing info
            progress_bar.update(1)
            current_avg_time = (
                (time.perf_counter() - start_time) / progress_bar.n
                if progress_bar.n > 0
                else 0
            )
            progress_bar.set_postfix(
                {
                    "Page Time": f"{page_time:.2f}s",
                    "Avg Time": f"{current_avg_time:.2f}s",
                }
            )

        progress_bar.close()

    total_time = time.perf_counter() - start_time

    # Calculate and display performance metrics
    avg_time_per_page = total_time / total_pages
    pages_per_second = total_pages / total_time if total_time > 0 else 0

    print("\nProcessing completed!")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Average time per page: {avg_time_per_page:.2f} seconds")
    print(f"Throughput: {pages_per_second:.2f} pages/second")


def main() -> None:
    """Main entry point for the PDF OCR AI application.

    Parses command line arguments and processes the PDF file using the specified AI provider.
    """
    parser = argparse.ArgumentParser(
        description="Convert PDF documents to Markdown using OCR capabilities powered by various AI providers"
    )
    parser.add_argument("input_pdf", help="Input PDF file path")
    parser.add_argument("output_md", help="Output Markdown file path")
    parser.add_argument(
        "--provider",
        default="lm-studio",
        choices=["lm-studio", "ollama", "llama.cpp"],
        help="AI provider to use for OCR (default: lm-studio)"
    )
    parser.add_argument(
        "--provider-url",
        help="Custom provider URL (default depends on provider type)"
    )
    parser.add_argument(
        "--model",
        default="qwen/qwen3-vl-30b",
        help="Model to use with the selected provider (default: qwen/qwen3-vl-30b)",
    )
    parser.add_argument(
        "--dpi", type=int, default=300, help="DPI for image conversion (default: 300)"
    )

    args = parser.parse_args()

    pdf_path = args.input_pdf
    output_md_path = args.output_md
    provider_type = args.provider
    provider_url = args.provider_url
    model = args.model
    dpi = args.dpi

    if not Path(pdf_path).exists():
        print(f"Error: PDF file '{pdf_path}' does not exist")
        sys.exit(1)

    process_pdf_to_markdown(pdf_path, output_md_path, provider_type, model, provider_url, dpi)
    print(f"\nMarkdown output saved to {output_md_path}")


if __name__ == "__main__":
    main()