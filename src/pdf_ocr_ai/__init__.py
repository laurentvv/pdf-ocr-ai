"""
PDF OCR AI - Multi-provider PDF to Markdown converter

This package provides OCR capabilities using multiple AI providers:
- LM Studio
- Ollama
- llama.cpp
"""

from .main import main, convert_pdf_to_markdown, process_pdf_to_markdown
from .providers import (
    get_provider,
    AIProvider,
    LMStudioProvider,
    OllamaProvider,
    LlamaCppProvider,
)

__all__ = [
    "main",
    "convert_pdf_to_markdown",
    "process_pdf_to_markdown",
    "get_provider",
    "AIProvider",
    "LMStudioProvider",
    "OllamaProvider",
    "LlamaCppProvider",
]
