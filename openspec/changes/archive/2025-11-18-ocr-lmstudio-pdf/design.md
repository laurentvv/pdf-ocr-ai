# OCR LMStudio PDF Design Document

## Overview
This document details the architectural design for implementing OCR functionality using LMStudio with the qwen/qwen3-vl-30b model in the PDF-to-Markdown converter.

## Architecture

### Current State
The existing system processes PDFs using traditional text extraction methods, which work well for text-based PDFs but struggle with scanned documents or those containing complex images.

### Proposed Architecture
```
PDF Input -> Page Extraction -> Image Conversion -> LMStudio API -> Text Processing -> Markdown Output
```

### Components

#### 1. PDF Page Extractor
- Utilizes PyMuPDF to extract each page as a high-resolution image
- Handles various PDF formats and structures
- Manages memory efficiently for large documents

#### 2. Image Processor
- Converts PDF pages to PNG images at 300 DPI for optimal OCR quality
- Encodes images to base64 format for API transmission
- Optimizes image size to balance quality with API request speed

#### 3. LMStudio API Client
- Configured to communicate with the local LMStudio instance at http://localhost:1234/v1
- Implements OpenAI-compatible API calls
- Handles authentication with the default LMStudio key

#### 4. Prompt Engine
- Creates specialized prompts for different document elements
- Optimizes prompts for text extraction, UI element recognition, and structure preservation
- Adapts prompts based on document characteristics

#### 5. Response Processor
- Parses model responses into structured data
- Converts responses to Markdown format
- Maintains document hierarchy and formatting

## Data Flow

1. The system loads a PDF file using PyMuPDF
2. Each page is converted to a high-resolution image (300 DPI)
3. The image is encoded to base64 format
4. The image and prompt are sent to the LMStudio vision model via API
5. The model processes the image and returns structured text content
6. The response is formatted into Markdown and stored
7. All pages are combined into a single Markdown output file

## Error Handling

- API request timeouts with retry logic
- Fallback processing for API failures
- Graceful degradation when LMStudio is unavailable
- Proper handling of malformed PDFs or images

## Scalability Considerations

- Page-by-page processing to manage memory usage for large PDFs
- Configurable processing parameters for different hardware capabilities
- Asynchronous API requests for improved performance

## Security Considerations

- All processing occurs locally with no external data transmission
- API communication only with local LMStudio instance
- No persistent storage of sensitive document content