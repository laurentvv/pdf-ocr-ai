import logging
import sys
import os
from unittest.mock import MagicMock, patch
import io

# Mock dependencies
sys.modules["fitz"] = MagicMock()
sys.modules["tqdm"] = MagicMock()
sys.modules["openai"] = MagicMock()

# Add the src directory to the path if needed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pdf_ocr_ai.providers import OpenAICompatibleProvider


def test_security_logging():
    """Test that sensitive information is not logged when an exception occurs"""
    print("Testing security logging...")

    # Setup logging to capture output in a buffer
    log_capture = io.StringIO()
    logger = logging.getLogger("pdf_ocr_ai.providers")
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)

    sensitive_key = "sk-sensitive-api-key-99999"
    provider = OpenAICompatibleProvider(
        base_url="http://localhost:1234/v1", api_key=sensitive_key
    )

    with patch.object(provider.client.chat.completions, "create") as mock_create:
        sensitive_msg = f"Forbidden: API Key {sensitive_key} is invalid"
        mock_create.side_effect = Exception(sensitive_msg)

        try:
            provider.ocr_image(b"fake_data", model="test-model", max_retries=1)
        except Exception:
            pass

    log_output = log_capture.getvalue()

    # Clean up logger
    logger.removeHandler(handler)

    # Assertions
    assert sensitive_key not in log_output, "Sensitive API key found in logs!"
    assert "Exception" in log_output, "Exception type should be logged"

    print(
        "✓ Security logging test passed: Sensitive information was not leaked to logs."
    )


if __name__ == "__main__":
    try:
        test_security_logging()
    except AssertionError as e:
        print(f"✗ Security logging test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")
        sys.exit(1)
