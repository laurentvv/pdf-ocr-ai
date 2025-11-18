"""
AI Provider interface and implementations for PDF OCR
"""
from abc import ABC, abstractmethod
import base64
import time
from pathlib import Path
from typing import Optional

from openai import OpenAI


class AIProvider(ABC):
    """Abstract base class for AI providers"""

    @abstractmethod
    def __init__(self, base_url: str, api_key: Optional[str] = None, **kwargs):
        pass

    @abstractmethod
    def ocr_image(self, image_bytes: bytes, model: str, **kwargs) -> str:
        """
        Process an image with OCR and return extracted text
        """
        pass


class LMStudioProvider(AIProvider):
    """LM Studio provider implementation"""

    def __init__(self, base_url: str = "http://localhost:1234/v1", api_key: Optional[str] = None, **kwargs):
        # LM Studio typically doesn't require an API key, but we pass a default one to satisfy OpenAI client
        effective_api_key = api_key or "lm-studio"
        self.client = OpenAI(base_url=base_url, api_key=effective_api_key)

    def ocr_image(self, image_bytes: bytes, model: str, max_retries: int = 3, **kwargs) -> str:
        """Use LM Studio vision model to extract raw text and UI information."""
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

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
                response = self.client.chat.completions.create(
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


class OllamaProvider(AIProvider):
    """Ollama provider implementation"""

    def __init__(self, base_url: str = "http://localhost:11434/v1", api_key: Optional[str] = None, **kwargs):
        # Ollama typically doesn't require an API key, but we pass a dummy one to satisfy OpenAI client
        effective_api_key = api_key or "ollama"
        self.client = OpenAI(base_url=base_url, api_key=effective_api_key)

    def ocr_image(self, image_bytes: bytes, model: str, max_retries: int = 3, **kwargs) -> str:
        """Use Ollama vision model to extract raw text and UI information."""
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

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
                response = self.client.chat.completions.create(
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


class LlamaCppProvider(AIProvider):
    """llama.cpp provider implementation"""

    def __init__(self, base_url: str = "http://localhost:8080/v1", api_key: Optional[str] = None, **kwargs):
        # llama.cpp typically doesn't require an API key, but we pass a dummy one to satisfy OpenAI client
        effective_api_key = api_key or "no-key"
        self.client = OpenAI(base_url=base_url, api_key=effective_api_key)

    def ocr_image(self, image_bytes: bytes, model: str, max_retries: int = 3, **kwargs) -> str:
        """Use llama.cpp vision model to extract raw text and UI information."""
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

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
                response = self.client.chat.completions.create(
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


def get_provider(provider_type: str, base_url: Optional[str] = None, api_key: Optional[str] = None) -> AIProvider:
    """Factory function to get the appropriate provider based on the type"""
    if provider_type.lower() == "lm-studio":
        url = base_url or "http://localhost:1234/v1"
        return LMStudioProvider(base_url=url, api_key=api_key)
    elif provider_type.lower() == "ollama":
        url = base_url or "http://localhost:11434/v1"
        return OllamaProvider(base_url=url, api_key=api_key)
    elif provider_type.lower() == "llama.cpp":
        url = base_url or "http://localhost:8080/v1"
        return LlamaCppProvider(base_url=url, api_key=api_key)
    else:
        raise ValueError(f"Unsupported provider: {provider_type}. Supported providers: lm-studio, ollama, llama.cpp")