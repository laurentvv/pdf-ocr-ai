import argparse
import base64
import sys
import time
from pathlib import Path

import fitz  # PyMuPDF
from openai import OpenAI
from tqdm import tqdm


def pdf_to_images(pdf_path, dpi=300):
    """Convert PDF pages to PNG images in memory."""
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


def image_to_base64(image_bytes):
    """Convert image bytes to base64 string for LM Studio."""
    return base64.b64encode(image_bytes).decode("utf-8")


def ocr_with_lmstudio(image_bytes, model="qwen/qwen3-vl-30b", max_retries=3):
    """Use LM Studio vision model to extract raw text and UI information."""
    base64_image = image_to_base64(image_bytes)

    # Initialize OpenAI client pointing to LM Studio
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    # Prompt focused on extracting raw text and especially UI screenshots/elements
    prompt = """
    Perform OCR on this image (which is a PDF page). Extract all raw text verbatim.
    If there are UI screenshots or interface elements (like buttons, menus, windows, code snippets), describe them in detail:
    - Identify UI components (e.g., buttons, text fields, icons).
    - Extract any text from UI elements.
    - Describe layouts, hierarchies, and any visible interactions.
    Output in structured Markdown: Use # for page header, ## for sections like 'Raw Text' and 'UI Descriptions'.
    Keep it concise but comprehensive.
    All responses must be in French as the document is in French.
    """

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{base64_image}"
                                },
                            },
                        ],
                    }
                ],
                max_tokens=2048,
                timeout=60,  # Set appropriate timeout
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retry
            else:
                raise e


def process_pdf_to_markdown(
    pdf_path, output_md_path, model="qwen/qwen3-vl-30b", dpi=300
):
    """Main function to process PDF and generate Markdown with progress tracking."""
    start_time = time.perf_counter()
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
            ocr_result = ocr_with_lmstudio(img_bytes, model)
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


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF documents to Markdown using OCR capabilities powered by LM Studio"
    )
    parser.add_argument("input_pdf", help="Input PDF file path")
    parser.add_argument("output_md", help="Output Markdown file path")
    parser.add_argument(
        "--model",
        default="qwen/qwen3-vl-30b",
        help="Model to use in LM Studio (default: qwen/qwen3-vl-30b)",
    )
    parser.add_argument(
        "--dpi", type=int, default=300, help="DPI for image conversion (default: 300)"
    )

    args = parser.parse_args()

    pdf_path = args.input_pdf
    output_md_path = args.output_md
    model = args.model
    dpi = args.dpi

    if not Path(pdf_path).exists():
        print(f"Error: PDF file '{pdf_path}' does not exist")
        sys.exit(1)

    process_pdf_to_markdown(pdf_path, output_md_path, model, dpi)
    print(f"\nMarkdown output saved to {output_md_path}")


if __name__ == "__main__":
    main()
