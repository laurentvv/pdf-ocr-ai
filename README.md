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

## Installation

You can use this tool in several ways:

### Option 1: Direct execution with uvx (no installation needed)
```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md>
```

### Option 2: Install as a tool with uv
```bash
uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr
# Then use: pdf-ocr-lmstudio <input.pdf> <output.md>
```

### Option 3: Traditional installation
1. Clone the repository and install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   OR with uv:
   ```bash
   uv sync
   ```

2. Start LM Studio locally and load the `qwen/qwen3-vl-30b` model

### Note on requirements.txt and pyproject.toml
This project now uses `pyproject.toml` as the primary source for dependencies and project metadata. The `requirements.txt` file is maintained for backward compatibility with older pip versions. For new installations, the `pyproject.toml` file will be used automatically by modern tools like uv.

## Usage

After traditional installation:
```bash
python pdf_ocr_lmstudio.py <input.pdf> <output.md>
```

After installing with uv tool:
```bash
pdf-ocr-lmstudio <input.pdf> <output.md>
```

### Example:
```bash
# Traditional installation
python pdf_ocr_lmstudio.py document.pdf output.md

# Or with directly executed via uvx
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md

# Or if installed via uv tool
pdf-ocr-lmstudio document.pdf output.md
```

## Prerequisites

- Python 3.13+ (for traditional installation)
- uv (for uv installation methods)
- LM Studio running locally with qwen/qwen3-vl-30b model loaded
- The qwen/qwen3-vl-30b model must be available in LM Studio

## Development Setup

### Virtual Environment Setup (Traditional Method)
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -e .
   ```

### Virtual Environment Setup (uv Method)
1. Create a virtual environment with uv:
   ```bash
   uv venv
   ```
2. Activate the environment (uv will use its own virtual environment management)
3. Install dependencies:
   ```bash
   uv sync
   ```

### VSCode Users on Windows
When using uv virtual environments, you may need to manually select the Python interpreter in VSCode:
1. Open VSCode in the project directory
2. Press `Ctrl+Shift+P` to open the command palette
3. Type "Python: Select Interpreter" and select it
4. Choose the interpreter from your uv virtual environment
   - You can locate it by running `uv venv --path` to see the environment location
   - The Python interpreter will typically be in `.venv\Scripts\python.exe` (when using `uv venv .venv`) or in a path like `%USERPROFILE%\AppData\Local\uv\...` when using global uv environments (Windows)
   - For macOS/Linux, the Python interpreter will be in `bin/python`

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

## Performance Considerations

- Large PDFs (>100 pages) may require substantial memory (several GB)
- Processing time is approximately 10-30 seconds per page depending on complexity
- For large documents, consider processing in batches or using a machine with sufficient RAM
- Processing speed depends on document complexity and hardware
- High DPI images (300 DPI) provide better OCR accuracy but take more time
- The first run may be slower as models are loaded into memory

## Advanced Configuration

The script uses the following default settings, which can be modified in the source code:
- DPI: 300 (for image quality)
- Model: qwen/qwen3-vl-30b (changeable in source)
- Max tokens: 2048
- Timeout: 60 seconds
- Retry attempts: 3

## Troubleshooting

- If you get API connection errors, ensure LM Studio is running and the correct model is loaded
- If processing fails, check that the model name in the script matches the one in LM Studio
- For large PDFs, ensure you have at least 1GB of RAM per 50 pages
- Consider closing other applications before processing large documents
- If you encounter memory errors, try processing smaller PDFs
- Very large PDFs may require more memory and processing time
- Ensure you have tqdm installed for progress tracking functionality
- When using uv, make sure uv is properly installed: `pip install uv`

## Migrating from Traditional .venv to uv

If you have an existing `.venv` directory and want to switch to uv-based environment management:

1. Backup your current setup if needed
2. Keep your existing `.venv` if you want to return to it later
3. Use uv commands instead:
   ```bash
   uv venv  # Create new environment managed by uv
   uv sync  # Install dependencies with uv
   ```
4. When activating environments, use uv commands or manually select the interpreter in your IDE

## Dependencies

- `openai`: For API communication with LM Studio
- `PyMuPDF`: For PDF processing and image extraction
- `tqdm`: For progress bar visualization