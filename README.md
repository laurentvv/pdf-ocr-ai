# PDF to Markdown OCR

[![GitHub](https://img.shields.io/badge/GitHub-Repository-333333?logo=github)](https://github.com/laurentvv/pdf-to-md-ocr)

This project converts PDF documents to Markdown using OCR capabilities powered by LM Studio with the qwen/qwen3-vl-30b model.

## Features

- Extracts text from PDF documents using AI-powered OCR
- Processes both text-based and scanned PDFs
- Identifies and describes UI elements in document screenshots
- Generates structured Markdown output preserving document hierarchy
- Handles multi-page PDFs with individual page processing
- Real-time progress tracking with percentage and ETA
- Time calculation for individual pages and overall processing
- Performance metrics including pages per second and average processing time

## Prerequisites

- Python 3.13+
- LM Studio running locally with qwen/qwen3-vl-30b model loaded
- The qwen/qwen3-vl-30b model must be available in LM Studio

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start LM Studio locally and load the `qwen/qwen3-vl-30b` model

## Usage

```bash
python pdf_ocr_lmstudio.py <input.pdf> <output.md>
```

### Example:
```bash
python pdf_ocr_lmstudio.py document.pdf output.md
```

## Setup LM Studio

1. Download and install [LM Studio](https://lmstudio.ai/)
2. In LM Studio, download the `qwen/qwen3-vl-30b` model
3. Start the local server with the model loaded
4. The script will automatically connect to the API at `http://localhost:1234/v1`

## How It Works

1. The script converts each PDF page to a high-resolution (300 DPI) image
2. Each image is sent to the LM Studio vision model via API
3. The AI model performs OCR and identifies UI elements in the images
4. The results are formatted as structured Markdown
5. All pages are combined into a single Markdown output file
6. Progress is displayed in real-time with estimated time remaining
7. Performance metrics are calculated and displayed upon completion

## Progress Tracking

The script includes comprehensive progress tracking:
- Visual progress bar showing percentage complete
- Time remaining estimate (ETA)
- Individual page processing time
- Average processing time per page
- Overall performance metrics at completion

## Troubleshooting

- If you get API connection errors, ensure LM Studio is running and the correct model is loaded
- If processing fails, check that the model name in the script matches the one in LM Studio
- Very large PDFs may require more memory and processing time
- Ensure you have tqdm installed for progress tracking functionality

## Dependencies

- `openai`: For API communication with LM Studio
- `PyMuPDF`: For PDF processing and image extraction
- `tqdm`: For progress bar visualization