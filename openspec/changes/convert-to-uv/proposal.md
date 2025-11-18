# Change: Convert Project from pip to uv

## Summary
Convert the pdf-to-md-ocr project from pip-based dependency management to uv-based management. This enables the project to be used as a command-line tool via `uvx` and `uv tool install`, improving accessibility and distribution.

## Context
The project currently uses `requirements.txt` for dependency management, requiring manual installation steps. Users cannot easily execute the tool without explicitly installing dependencies first. The proposed change will modernize the packaging approach and enable easier execution.

## Requirements
1. Project must be installable via `uv` with proper `pyproject.toml`
2. Command-line interface must be accessible via `uvx`
3. Tool must be installable via `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr`
4. Backward compatibility must be maintained with existing command-line interface
5. All current functionality must remain intact
6. Virtual environment management must be updated to use uv standards while maintaining compatibility
7. Documentation must provide clear instructions for VSCode users on Windows regarding uv virtual environment recognition
8. Existing `.venv` directories must be preserved during transition and a migration path provided
9. Both README.md and README_FR.md must be updated with uv installation and usage instructions

## Approach
- Create proper `pyproject.toml` with project metadata and dependencies
- Define console script entry point for command-line access
- Maintain existing functionality while enabling new distribution methods
- Preserve existing command-line interface for backward compatibility

## Validation
- Verify `uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md>` works
- Verify `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr` works
- Ensure existing `python pdf_ocr_lmstudio.py <input.pdf> <output.md>` still works
- Test dependency installation with `uv sync`