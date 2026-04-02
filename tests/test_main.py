import sys
from unittest.mock import patch, MagicMock
from pathlib import Path
import pytest

# Mock all dependencies
sys.modules["fitz"] = MagicMock()
sys.modules["tqdm"] = MagicMock()
sys.modules["openai"] = MagicMock()

from pdf_ocr_ai.main import main

def test_main_missing_pdf():
    """Test that main exits with code 1 when the PDF file does not exist."""
    test_args = ["pdf-ocr-ai", "non_existent.pdf", "output.md"]

    with patch("sys.argv", test_args):
        # Patching Path.exists in pdf_ocr_ai.main
        with patch("pdf_ocr_ai.main.Path.exists") as mock_exists:
            mock_exists.return_value = False
            with patch("builtins.print") as mock_print:
                with pytest.raises(SystemExit) as excinfo:
                    main()

                assert excinfo.value.code == 1
                mock_print.assert_called_once_with("Error: PDF file 'non_existent.pdf' does not exist")

def test_main_existing_pdf_calls_process(tmp_path):
    """Test that main calls process_pdf_to_markdown when the PDF file exists."""
    pdf_file = tmp_path / "test.pdf"
    pdf_file.write_text("dummy content")
    output_md = tmp_path / "output.md"

    test_args = ["pdf-ocr-ai", str(pdf_file), str(output_md)]

    with patch("sys.argv", test_args):
        # We need to ensure Path.exists returns True for this test
        with patch("pdf_ocr_ai.main.Path.exists") as mock_exists:
            mock_exists.return_value = True
            with patch("pdf_ocr_ai.main.process_pdf_to_markdown") as mock_process:
                with patch("builtins.print"):
                    main()
                    mock_process.assert_called_once_with(
                        str(pdf_file), str(output_md), "lm-studio", "qwen/qwen3-vl-30b", None, 300
                    )
