# Project Summary

## Overall Goal
Convert the PDF to Markdown OCR project from pip-based dependency management to uv-based management, enabling the project to be used with `uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md>` and `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr`, while maintaining backward compatibility and improving documentation and packaging standards.

## Key Knowledge
- **Technology Stack**: Python 3.13+, LM Studio with qwen/qwen3-vl-30b model, PyMuPDF, OpenAI API, tqdm
- **Packaging**: pyproject.toml with setuptools.build_meta backend, console script entry point `pdf-ocr-lmstudio = pdf_ocr_lmstudio:main`
- **Source Code**: Located in `src/pdf_ocr_lmstudio/__init__.py` with package structure in `src/`
- **Command Line Options**: `--model <model_name>` (default: qwen/qwen3-vl-30b) and `--dpi <value>` (default: 300)
- **Installation Methods**: (1) uvx direct execution, (2) uv tool install, (3) traditional pip install
- **Dependencies**: openai>=1.50.0, PyMuPDF>=1.23.0, tqdm>=4.66.0 + optional dev dependencies
- **Documentation**: Enhanced README with uvx/uv tool installation prominently featured, performance considerations, configuration options
- **Environment**: Supports both traditional .venv and uv environment management with migration guidance

## Recent Actions
- [DONE] Created proper pyproject.toml with project metadata, dependencies, and console script entry point
- [DONE] Restructured project with proper package structure (`src/pdf_ocr_lmstudio/`)
- [DONE] Added command-line argument support for `--model` and `--dpi` parameters using argparse
- [DONE] Enhanced README files in both English and French with better formatting, badges, tables, and installation guidance
- [DONE] Migrated from requirements.txt to pyproject.toml-only dependency management
- [DONE] Improved installation instructions with emphasis on uv and uvx methods over traditional installation
- [DONE] Enhanced troubleshooting and performance considerations sections
- [DONE] Added comprehensive documentation for uv tool management commands
- [DONE] Archived the OpenSpec change proposal for the conversion to uv in `openspec/changes/archive/convert-to-uv/`

## Current Plan
- [DONE] Complete the conversion from pip to uv-based dependency management
- [DONE] Ensure backward compatibility while promoting modern uv usage
- [DONE] Update all documentation to reflect new installation and usage patterns
- [DONE] Archive the OpenSpec change proposal as completed

---

## Summary Metadata
**Update time**: 2025-11-18T15:36:58.102Z 
