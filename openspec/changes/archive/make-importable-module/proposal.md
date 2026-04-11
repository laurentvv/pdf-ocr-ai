# Change: Make PDF OCR AI an Importable Python Module

## Why
Currently, the `pdf-ocr-ai` tool is strictly designed as a command-line interface (CLI). It processes a PDF and writes the output directly to a Markdown file while printing progress to the console. To increase its utility and allow developers to integrate the OCR functionality into other Python applications, it needs to be accessible as a reusable, importable module that returns the processed text directly.

## What Changes
- Refactor `main.py` to decouple the OCR extraction logic from the file output and CLI console printing.
- Create a new `convert_pdf_to_markdown` function that returns the extracted Markdown as a string and allows hiding the progress bar.
- Update `process_pdf_to_markdown` to use the new function while retaining the existing CLI behavior.
- Export `convert_pdf_to_markdown` in `__init__.py`.
- Add documentation in `README.md` for using it as a library and instructions for deploying to PyPI.

## Impact
- Affected specs: `library` (new capability added).
- Affected code: `src/pdf_ocr_ai/main.py`, `src/pdf_ocr_ai/__init__.py`, `README.md`.
