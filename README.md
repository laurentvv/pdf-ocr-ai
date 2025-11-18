<div align="center">

# 📄 PDF to Markdown OCR

[![GitHub](https://img.shields.io/badge/GitHub-Repository-333333?logo=github)](https://github.com/laurentvv/pdf-to-md-ocr)
[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-Modern%20package%20manager-00a8ff?logo=python)](https://github.com/astral-sh/uv)

**Convert PDF documents to Markdown using OCR capabilities powered by LM Studio**

*Powered by AI models for accurate text extraction and UI element recognition*

</div>

---

## ✨ Features

<div align="center">

| Feature | Description |
|--------|-------------|
| 🧠 **AI-Powered OCR** | Extracts text from PDF documents using advanced AI models |
| 🔍 **Multi-Format Support** | Processes both text-based and scanned PDFs |
| 💻 **UI Element Recognition** | Identifies and describes UI elements in document screenshots |
| 📝 **Structured Output** | Generates structured Markdown preserving document hierarchy |
| 📄 **Multi-Page Handling** | Handles multi-page PDFs with individual page processing |
| 📊 **Progress Tracking** | Real-time progress tracking with percentage and ETA |
| ⚡ **Performance Metrics** | Time calculation and performance analytics |

</div>

## Prerequisites

### Core Requirements
- **Python 3.13+** (required for traditional installation methods)
- **LM Studio** running locally with the `qwen/qwen3-vl-30b` model loaded
- **Hardware**: Sufficient RAM and VRAM for processing PDFs (recommended: 16GB+ RAM for large documents)

### Installation-Specific Requirements

#### For uv-based methods (recommended):
- **uv package manager** installed (install with: `pip install uv`)
- LM Studio with `qwen/qwen3-vl-30b` model loaded

#### For traditional methods:
- **pip** package manager
- Git for cloning the repository (if cloning)
- LM Studio with `qwen/qwen3-vl-30b` model loaded

### Setup LM Studio
Before using the tool, you need to set up LM Studio:
1. Download and install [LM Studio](https://lmstudio.ai/)
2. In LM Studio, download the `qwen/qwen3-vl-30b` model (this is the recommended model for optimal results)
3. Start the local server with the model loaded:
   - Open LM Studio
   - Select the `qwen/qwen3-vl-30b` model from your model list
   - Click on the "Load" button to load the model
   - Click on the "Start Server" button to start the local API server
4. The script will automatically connect to the API at `http://localhost:1234/v1`
5. Ensure the "Enable remote access (allows external connections)" is unchecked for local use
6. For best results, ensure you have sufficient VRAM allocated to the model in LM Studio

## 🚀 Installation

For the best experience, we recommend using uv-based methods. These approaches provide better dependency management and easier usage:

### 🥇 Option 1: Direct execution with uvx (Recommended - No Installation Required)

Execute the tool directly from the git repository without any local installation. This is the simplest way to use the tool:

<div align="center">

```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md>
```

</div>

<details>
<summary><b>Why this approach?</b></summary>

- ✅ No local installation required
- ✅ Always uses the latest version
- ✅ Automatic dependency resolution
- ✅ No conflicts with other Python projects
- ✅ Perfect for one-time usage

</details>

---

### 🥈 Option 2: Install as a tool with uv (Recommended for Regular Use)

This method permanently installs the tool in your environment, making it available as a command-line utility.

<div align="center">

```bash
uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr
```

</div>

<details>
<summary><b>Benefits of this approach</b></summary>

- ✅ Command `pdf-ocr-lmstudio` becomes globally available
- ✅ uv manages dependencies automatically in isolated environment
- ✅ No need to reinstall each time you use the tool
- ✅ Better dependency isolation than traditional pip
- ✅ Easy to update or remove the tool
- ✅ Perfect for regular usage

</details>

<div align="center">

**Use after installation:**
```bash
pdf-ocr-lmstudio <input.pdf> <output.md>
```

</div>

#### Tool Management Commands

<div align="center">

| Command | Description |
|--------|-------------|
| `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr` | Install the tool |
| `uv tool install --force-reinstall git+https://github.com/laurentvv/pdf-to-md-ocr` | Update the tool |
| `uv tool uninstall pdf-ocr-lmstudio` | Remove the tool |

</div>

---

### 🥉 Option 3: Traditional Installation (For Development)

Only recommended if you plan to modify the code or work with a virtual environment:

1. Clone the repository and install the required dependencies from pyproject.toml:
   ```bash
   pip install .
   ```
   OR with uv:
   ```bash
   uv sync
   ```

2. Start LM Studio locally and load the `qwen/qwen3-vl-30b` model

## 📋 Usage

<div align="center">

For the best experience, we recommend using uv-based methods:

### 🎯 Primary Command (uvx - No Installation Required)
```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md> [options]
```

### 🧰 Installed Tool (After `uv tool install`)
```bash
pdf-ocr-lmstudio <input.pdf> <output.md> [options]
```

</div>

---

### ⚙️ Command Line Options

<div align="center">

| Option | Description | Default |
|--------|-------------|---------|
| `--model <model_name>` | Specify the model to use in LM Studio | `qwen/qwen3-vl-30b` |
| `--dpi <value>` | Set DPI for image conversion | `300` |

</div>

---

### 💡 Examples

<div align="center">

#### Quick Start
```bash
# Direct execution with uvx (no installation needed)
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md
```

#### Advanced Usage
```bash
# With custom model using uvx
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md --model "llama/llama3.2-vision"

# With custom DPI using uvx
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md --dpi 200

# With both custom model and DPI using uvx
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio document.pdf output.md --model "llama/llama3.2-vision" --dpi 150
```

#### With Installed Tool
```bash
# After installing via uv tool
pdf-ocr-lmstudio document.pdf output.md --model "llama/llama3.2-vision"
```

</div>

## Prerequisites

- Python 3.13+ (for traditional installation)
- uv (for uv installation methods)
- LM Studio running locally with the qwen/qwen3-vl-30b model loaded
- The qwen/qwen3-vl-30b model must be available in LM Studio (see Setup LM Studio section below)
- Local LM Studio server running with the model loaded (default API endpoint: http://localhost:1234/v1)

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
2. In LM Studio, download the `qwen/qwen3-vl-30b` model (this is the recommended model for optimal results)
3. Start the local server with the model loaded:
   - Open LM Studio
   - Select the `qwen/qwen3-vl-30b` model from your model list
   - Click on the "Load" button to load the model
   - Click on the "Start Server" button to start the local API server
4. The script will automatically connect to the API at `http://localhost:1234/v1`
5. Ensure the "Enable remote access (allows external connections)" is unchecked for local use
6. For best results, ensure you have sufficient VRAM allocated to the model in LM Studio

## 🔬 How It Works

<div align="center">

| Step | Description |
|------|-------------|
| 1️⃣ | The script converts each PDF page to a high-resolution (300 DPI) image |
| 2️⃣ | Each image is sent to the LM Studio vision model via API |
| 3️⃣ | The AI model performs OCR and identifies UI elements in the images |
| 4️⃣ | The results are formatted as structured Markdown |
| 5️⃣ | All pages are combined into a single Markdown output file |
| 6️⃣ | Progress is displayed in real-time with estimated time remaining |
| 7️⃣ | Performance metrics are calculated and displayed upon completion |

</div>

## 📊 Progress Tracking

<div align="center">

| Feature | Description |
|--------|-------------|
| 📈 **Visual Progress Bar** | Shows percentage complete in real-time |
| ⏳ **ETA** | Time remaining estimate |
| ⏱️ **Per-Page Timing** | Individual page processing time |
| 📉 **Average Timing** | Average processing time per page |
| 📋 **Performance Summary** | Overall metrics at completion |

</div>

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

## 🛠️ Troubleshooting

<div align="center">

| Issue | Solution |
|-------|----------|
| 🔌 **API Connection Errors** | Ensure LM Studio is running and the correct model is loaded |
| ❌ **Processing Fails** | Check that the model name in command matches the one in LM Studio |
| 💾 **Memory Issues** | For large PDFs, ensure you have at least 1GB of RAM per 50 pages |
| 🧠 **Model Not Found** | Verify the model name matches exactly what's available in LM Studio |
| ⚠️ **Performance Issues** | Close other applications before processing large documents |
| 🚫 **Memory Errors** | Try processing smaller PDFs or increase system resources |
| 📊 **Progress Bar Missing** | Ensure tqdm is available in your Python environment |
| 🐍 **uv Installation Issues** | Make sure uv is properly installed: `pip install uv` |

</div>

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