"""
PDF to Markdown OCR - Main processing module

This module provides functions for converting PDF files to Markdown format
using AI-powered OCR from multiple providers.
"""

import argparse
import sys
import time
from pathlib import Path
from typing import Generator, Tuple, Union

import fitz  # PyMuPDF
from tqdm import tqdm

from .providers import get_provider


def page_needs_ocr(page: fitz.Page) -> bool:
    """Determine if a PDF page requires AI OCR processing based on its content.

    Args:
        page: The PyMuPDF page object

    Returns:
        True if the page needs OCR (has images, drawings, or very little text), False otherwise.
    """
    # Check for images
    if len(page.get_images(full=True)) > 0:
        return True

    # Check for drawings/vector graphics
    if len(page.get_drawings()) > 0:
        return True

    # Check text density. If there's very little text, it might be a scanned image
    # without proper text layers, or just an empty page (which AI can describe or skip).
    text = page.get_text()
    if len(text.strip()) < 50:
        return True

    return False


def process_pdf_to_markdown(
    pdf_path: str,
    output_md_path: str,
    provider_type: str = "lm-studio",
    model: str = "qwen/qwen3-vl-30b",
    provider_url: str = None,
    dpi: int = 300,
) -> None:
    """Main function to process PDF and generate Markdown with progress tracking.
    Uses a hybrid approach: local extraction for simple text pages, AI OCR for complex ones.

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

    doc = fitz.open(pdf_path)
    total_pages = len(doc)

    print(f"Starting hybrid extraction processing for {total_pages} pages...")

    with open(output_md_path, "w", encoding="utf-8") as md_file:
        md_file.write(f"# OCR Extracted Content from {Path(pdf_path).name}\n\n")

        # Initialize progress bar
        progress_bar = tqdm(
            total=total_pages, desc="Processing pages", unit="page", leave=True
        )

        try:
            for page_num in range(total_pages):
                page_start_time = time.perf_counter()
                page = doc.load_page(page_num)

                md_file.write(f"## Page {page_num + 1}\n\n")

                # Hybrid Decision Logic
                if page_needs_ocr(page):
                    # Complex page -> use AI Vision
                    method = "AI OCR"
                    pix = page.get_pixmap(dpi=dpi, alpha=False)
                    img_bytes = pix.tobytes("png")
                    result = provider.ocr_image(img_bytes, model)
                else:
                    # Simple text page -> use local fast extraction
                    method = "Local"
                    # Try to get markdown if supported by the fitz version, else fallback to text
                    try:
                        result = page.get_text("markdown")
                    except ValueError:
                        # Fallback for older PyMuPDF versions
                        result = page.get_text("text")

                page_end_time = time.perf_counter()
                page_time = page_end_time - page_start_time

                md_file.write(result + "\n\n---\n\n")

                # Update progress bar with page processing info
                progress_bar.update(1)
                current_avg_time = (
                    (time.perf_counter() - start_time) / progress_bar.n
                    if progress_bar.n > 0
                    else 0
                )
                progress_bar.set_postfix(
                    {
                        "Method": method,
                        "Page Time": f"{page_time:.2f}s",
                        "Avg Time": f"{current_avg_time:.2f}s",
                    }
                )
        finally:
            progress_bar.close()
            doc.close()

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
        help="AI provider to use for OCR (default: lm-studio)",
    )
    parser.add_argument(
        "--provider-url", help="Custom provider URL (default depends on provider type)"
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

    process_pdf_to_markdown(
        pdf_path, output_md_path, provider_type, model, provider_url, dpi
    )
    print(f"\nMarkdown output saved to {output_md_path}")


if __name__ == "__main__":
    main()
