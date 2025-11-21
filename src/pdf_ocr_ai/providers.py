"""
AI Provider interface and implementations for PDF OCR
"""

import base64
import logging
import time
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from openai import OpenAI

logger = logging.getLogger(__name__)

# OCR prompt reused across all providers
OCR_PROMPT = """
Perform OCR on this image (which is a PDF page). Extract all raw text verbatim.
If there are UI screenshots or interface elements (like buttons, menus, windows, code snippets), describe them in detail:
- Identify UI components (e.g., buttons, text fields, icons).
- Extract any text from UI elements.
- Describe layouts, hierarchies, and any visible interactions.
Output in structured Markdown: Use # for page header, ## for sections like 'Raw Text' and 'UI Descriptions'.
Keep it concise but comprehensive.
All responses must be in French as the document is in French.
"""


class ProviderConfig:
    """Configuration constants for AI providers."""

    DEFAULT_RETRY_COUNT: int = 3
    DEFAULT_TIMEOUT: int = 600
    DEFAULT_MAX_TOKENS: int = 2048
    DEFAULT_LM_STUDIO_URL: str = "http://localhost:1234/v1"
    DEFAULT_OLLAMA_URL: str = "http://localhost:11434/v1"
    DEFAULT_LLAMA_CPP_URL: str = "http://localhost:8080/v1"


class AIProvider(ABC):
    """Abstract base class for AI providers"""

    def __init__(
        self, base_url: str, api_key: Optional[str] = None, **kwargs: Dict[str, Any]
    ) -> None:
        """Initialize the AI provider.

        Args:
            base_url: The API endpoint URL for the provider
            api_key: Authentication key (if required)
            **kwargs: Additional provider-specific parameters
        """
        pass

    @abstractmethod
    def ocr_image(
        self, image_bytes: bytes, model: str, **kwargs: Dict[str, Any]
    ) -> str:
        """Process an image with OCR and return extracted text.

        Args:
            image_bytes: Raw image bytes to process
            model: Name of the model to use
            **kwargs: Additional parameters for the OCR operation

        Returns:
            Extracted text in Markdown format

        Raises:
            Exception: If OCR operation fails after all retries
        """
        pass


class OpenAICompatibleProvider(AIProvider):
    """Base class for OpenAI-compatible providers"""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        default_api_key: str = "no-key",
        **kwargs,
    ):
        effective_api_key = api_key or default_api_key
        self.client = OpenAI(base_url=base_url, api_key=effective_api_key)
        self.default_api_key = default_api_key

    def ocr_image(
        self, image_bytes: bytes, model: str, max_retries: int = 3, **kwargs
    ) -> str:
        """Process an image with OCR and return extracted text.

        Args:
            image_bytes: Raw image bytes to process
            model: Name of the model to use
            max_retries: Maximum number of retry attempts (default: 3)
            **kwargs: Additional parameters for the OCR operation

        Returns:
            Extracted text in Markdown format

        Raises:
            Exception: If OCR operation fails after all retries
        """
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": OCR_PROMPT},
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

                content = response.choices[0].message.content
                if not content:
                    raise ValueError("Empty response from AI provider")

                return content

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed for model {model}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2**attempt)  # Exponential backoff
                else:
                    logger.error(f"All {max_retries} attempts failed for model {model}")
                    raise e


class LMStudioProvider(OpenAICompatibleProvider):
    """LM Studio provider implementation"""

    def __init__(
        self,
        base_url: str = "http://localhost:1234/v1",
        api_key: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(base_url, api_key, "lm-studio", **kwargs)


class OllamaProvider(OpenAICompatibleProvider):
    """Ollama provider implementation"""

    def __init__(
        self,
        base_url: str = "http://localhost:11434/v1",
        api_key: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(base_url, api_key, "ollama", **kwargs)


class LlamaCppProvider(OpenAICompatibleProvider):
    """llama.cpp provider implementation"""

    def __init__(
        self,
        base_url: str = "http://localhost:8080/v1",
        api_key: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(base_url, api_key, "no-key", **kwargs)


def get_provider(
    provider_type: str, base_url: Optional[str] = None, api_key: Optional[str] = None
) -> AIProvider:
    """Factory function to get the appropriate provider based on the type"""
    if provider_type.lower() == "lm-studio":
        url = base_url or ProviderConfig.DEFAULT_LM_STUDIO_URL
        return LMStudioProvider(base_url=url, api_key=api_key)
    elif provider_type.lower() == "ollama":
        url = base_url or ProviderConfig.DEFAULT_OLLAMA_URL
        return OllamaProvider(base_url=url, api_key=api_key)
    elif provider_type.lower() == "llama.cpp":
        url = base_url or ProviderConfig.DEFAULT_LLAMA_CPP_URL
        return LlamaCppProvider(base_url=url, api_key=api_key)
    else:
        raise ValueError(
            f"Unsupported provider: {provider_type}. Supported providers: lm-studio, ollama, llama.cpp"
        )
