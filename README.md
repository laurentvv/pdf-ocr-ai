<div align="center">

# 📄 PDF to Markdown OCR

[![GitHub](https://img.shields.io/badge/GitHub-Repository-333333?logo=github)](https://github.com/laurentvv/pdf-to-md-ocr)
[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/uv-Modern%20package%20manager-00a8ff?logo=python)](https://github.com/astral-sh/uv)

**Convert PDF documents to Markdown using OCR capabilities powered by multiple AI providers**

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
| 🔄 **Multi-Provider Support** | Works with LM Studio, Ollama, and llama.cpp |

</div>

## Prerequisites

### Core Requirements
- **Python 3.13+** (required for traditional installation methods)
- **One of the following AI providers**:
  - **LM Studio** running locally with a vision model (e.g., `qwen/qwen3-vl-30b`)
  - **Ollama** running locally with a vision model (e.g., `llava`)
  - **llama.cpp** running locally with a vision model
- **Hardware**: Sufficient RAM and VRAM for processing PDFs (recommended: 16GB+ RAM for large documents)

### Installation-Specific Requirements

#### For uv-based methods (recommended):
- **uv package manager** installed (install with: `pip install uv`)

#### For traditional methods:
- **pip** package manager
- Git for cloning the repository (if cloning)

## 🚀 Installation

For the best experience, we recommend using uv-based methods. These approaches provide better dependency management and easier usage:

### 🥇 Option 1: Direct execution with uvx (Recommended - No Installation Required)

Execute the tool directly from the git repository without any local installation. This is the simplest way to use the tool:

<div align="center">

```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai <input.pdf> <output.md>
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

- ✅ Command `pdf-ocr-ai` becomes globally available
- ✅ uv manages dependencies automatically in isolated environment
- ✅ No need to reinstall each time you use the tool
- ✅ Better dependency isolation than traditional pip
- ✅ Easy to update or remove the tool
- ✅ Perfect for regular usage

</details>

<div align="center">

**Use after installation:**
```bash
pdf-ocr-ai <input.pdf> <output.md>
```

</div>

#### Tool Management Commands

<div align="center">

| Command | Description |
|--------|-------------|
| `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr` | Install the tool |
| `uv tool install --force-reinstall git+https://github.com/laurentvv/pdf-to-md-ocr` | Update the tool |
| `uv tool uninstall pdf-ocr-ai` | Remove the tool |

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

## 📋 Usage

<div align="center">

For the best experience, we recommend using uv-based methods:

### 🎯 Primary Command (uvx - No Installation Required)
```bash
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai <input.pdf> <output.md> [options]
```

### 🧰 Installed Tool (After `uv tool install`)
```bash
pdf-ocr-ai <input.pdf> <output.md> [options]
```

### 🔄 Backward Compatibility
The tool also supports the original command name for backward compatibility:
```bash
pdf-ocr-lmstudio <input.pdf> <output.md> [options]
```

</div>

---

### ⚙️ Command Line Options

<div align="center">

| Option | Description | Default |
|--------|-------------|---------|
| `--provider` | AI provider to use: lm-studio, ollama, llama.cpp | `lm-studio` |
| `--provider-url` | Custom provider URL (default depends on provider) | See details below |
| `--model <model_name>` | Specify the model to use with the provider | `qwen/qwen3-vl-30b` |
| `--dpi <value>` | Set DPI for image conversion | `300` |

</div>

---

### 💡 Examples

<div align="center">

#### Quick Start with LM Studio
```bash
# Direct execution with uvx (no installation needed)
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md
```

#### Using Ollama
```bash
# With Ollama provider
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md --provider ollama --model llava

# With custom Ollama URL
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md --provider ollama --provider-url http://localhost:11434/v1 --model llava
```

#### Using llama.cpp
```bash
# With llama.cpp provider
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md --provider "llama.cpp" --model qwen2-vl
```

#### Advanced Usage
```bash
# With custom DPI
uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-ai document.pdf output.md --provider ollama --model llava --dpi 200

# Using the original command name (backward compatibility)
pdf-ocr-lmstudio document.pdf output.md --provider ollama --model llava
```

#### With Installed Tool
```bash
# After installing via uv tool
pdf-ocr-ai document.pdf output.md --provider ollama --model llava
```

</div>

## Setup AI Providers

### Setup LM Studio

1. Download and install [LM Studio](https://lmstudio.ai/)
2. In LM Studio, download a vision model (recommended: `qwen/qwen3-vl-30b`)
3. Start the local server with the model loaded:
   - Open LM Studio
   - Select your vision model from the model list
   - Click on the "Load" button to load the model
   - Click on the "Start Server" button to start the local API server
4. The script will automatically connect to the API at `http://localhost:1234/v1`
5. Ensure the "Enable remote access (allows external connections)" is unchecked for local use

### Setup Ollama

1. Download and install [Ollama](https://ollama.ai/)
2. Pull a vision model:
   ```bash
   ollama pull llava
   # or
   ollama pull qwen2-vl
   ```
3. Start Ollama (typically runs automatically after installation):
   ```bash
   ollama serve
   ```
4. The script will connect to the API at `http://localhost:11434/v1`

### Setup llama.cpp

1. Clone and build [llama.cpp](https://github.com/ggerganov/llama.cpp)
2. Build with server support:
   ```bash
   make
   cd examples/server
   make server
   ```
3. Run the server with a vision model:
   ```bash
   # Example command (adjust paths and parameters as needed)
   ./server -m path/to/model.gguf --port 8080
   ```
4. The script will connect to the API at `http://localhost:8080/v1`

## 🔬 How It Works

<div align="center">

| Step | Description |
|------|-------------|
| 1️⃣ | The script converts each PDF page to a high-resolution (300 DPI) image |
| 2️⃣ | Each image is sent to the selected AI provider's vision model via API |
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
- Processing time varies significantly depending on the AI provider and model used
- For large documents, consider processing in batches or using a machine with sufficient RAM
- Processing speed depends on document complexity, hardware, and AI provider performance
- High DPI images (300 DPI) provide better OCR accuracy but take more time
- The first run may be slower as models are loaded into memory

## Advanced Configuration

The script uses the following default settings, which can be modified in the source code:
- Default provider: lm-studio
- LM Studio URL: http://localhost:1234/v1
- Ollama URL: http://localhost:11434/v1
- llama.cpp URL: http://localhost:8080/v1
- DPI: 300 (for image quality)
- Model: qwen/qwen3-vl-30b (changeable in command)
- Max tokens: 2048
- Timeout: 60 seconds
- Retry attempts: 3

## 🛠️ Troubleshooting

<div align="center">

| Issue | Solution |
|-------|----------|
| 🔌 **API Connection Errors** | Ensure your selected AI provider (LM Studio/Ollama/llama.cpp) is running and accessible |
| ❌ **Processing Fails** | Check that the model name in command matches what's available in your provider |
| 💾 **Memory Issues** | For large PDFs, ensure you have at least 1GB of RAM per 50 pages |
| 🧠 **Model Not Found** | Verify the model name matches exactly what's available in your provider |
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

- `openai`: For API communication with AI providers
- `PyMuPDF`: For PDF processing and image extraction
- `tqdm`: For progress bar visualization