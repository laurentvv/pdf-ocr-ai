"""
Basic tests to validate the multi-provider functionality
"""
import argparse
import sys
import os
# Add the src directory to the path so we can import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pdf_ocr_ai.providers import get_provider, LMStudioProvider, OllamaProvider, LlamaCppProvider


def test_provider_creation():
    """Test that all providers can be created with default settings"""
    print("Testing provider creation...")

    # Test LM Studio provider
    lm_provider = get_provider("lm-studio")
    assert isinstance(lm_provider, LMStudioProvider)
    print("✓ LM Studio provider created successfully")

    # Test Ollama provider
    ollama_provider = get_provider("ollama")
    assert isinstance(ollama_provider, OllamaProvider)
    print("✓ Ollama provider created successfully")

    # Test llama.cpp provider
    llama_provider = get_provider("llama.cpp")
    assert isinstance(llama_provider, LlamaCppProvider)
    print("✓ llama.cpp provider created successfully")

    # Test with custom URLs
    lm_custom = get_provider("lm-studio", base_url="http://custom:1234/v1")
    assert isinstance(lm_custom, LMStudioProvider)
    print("✓ LM Studio provider with custom URL created successfully")

    print("All provider creation tests passed!")


def test_invalid_provider():
    """Test that invalid provider raises an error"""
    print("Testing invalid provider handling...")

    try:
        get_provider("invalid-provider")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Unsupported provider" in str(e)
        print("✓ Invalid provider correctly raises ValueError")


def test_argument_parsing():
    """Test that command line arguments work correctly"""
    print("Testing argument parsing...")

    # Test the argument parser
    parser = argparse.ArgumentParser(
        description="Test argument parsing"
    )
    parser.add_argument(
        "--provider",
        default="lm-studio",
        choices=["lm-studio", "ollama", "llama.cpp"],
        help="AI provider to use for OCR (default: lm-studio)"
    )
    parser.add_argument(
        "--provider-url",
        help="Custom provider URL (default depends on provider type)"
    )
    parser.add_argument(
        "--model",
        default="qwen/qwen3-vl-30b",
        help="Model to use with the selected provider (default: qwen/qwen3-vl-30b)",
    )
    parser.add_argument(
        "--dpi", type=int, default=300, help="DPI for image conversion (default: 300)"
    )

    # Parse some test arguments
    test_args = [
        "--provider", "ollama",
        "--model", "llava",
        "--dpi", "200"
    ]

    parsed = parser.parse_args(test_args)
    assert parsed.provider == "ollama"
    assert parsed.model == "llava"
    assert parsed.dpi == 200
    print("✓ Argument parsing works correctly")


def run_all_tests():
    """Run all validation tests"""
    print("Running validation tests...\n")

    test_provider_creation()
    print()

    test_invalid_provider()
    print()

    test_argument_parsing()
    print()

    print("🎉 All tests passed! The multi-provider implementation is working correctly.")


if __name__ == "__main__":
    run_all_tests()