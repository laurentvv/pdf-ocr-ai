## ADDED Requirements
### Requirement: Importable Python Module
The system SHALL provide an API that allows developers to import the PDF to Markdown conversion functionality directly into their Python code without triggering side-effects like writing to disk or printing to standard output unless explicitly requested.

#### Scenario: Basic Library Import
- **WHEN** a developer imports `convert_pdf_to_markdown` from `pdf_ocr_ai` and calls it with a valid PDF path
- **THEN** the function returns the extracted text as a Markdown string

#### Scenario: Hide Progress Bar
- **WHEN** a developer calls `convert_pdf_to_markdown` with `show_progress=False`
- **THEN** no progress bar or console output is generated during the extraction process
