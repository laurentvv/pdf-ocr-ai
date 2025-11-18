# Design: Convert Project from pip to uv

## Architecture Overview
The conversion will transform the project from a simple script with requirements.txt to a properly packaged Python application with pyproject.toml. The core OCR functionality remains unchanged, but the packaging enables new distribution and execution methods.

## Component Changes

### pyproject.toml Structure
The new `pyproject.toml` will include:
- Project metadata (name, version, description)
- Dependencies matching current requirements.txt
- Console script entry point definition
- Package metadata for PyPI compatibility

### Entry Point Mapping
Current execution: `python pdf_ocr_lmstudio.py <input.pdf> <output.md>`
New execution methods:
- `uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md>`
- `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr` followed by `pdf-ocr-lmstudio <input.pdf> <output.md>`
- Traditional: `python pdf_ocr_lmstudio.py <input.pdf> <output.md>` (maintained)

## Dependencies Mapping
Current `requirements.txt`:
- `openai>=1.0.0`
- `PyMuPDF>=1.23.0`
- `tqdm>=4.62.0`

These will be migrated to `[project.dependencies]` in pyproject.toml without functional changes.

## Backwards Compatibility
The design maintains full backwards compatibility:
- Existing command-line interface remains identical
- Function behavior unchanged
- Same parameters and return values
- No changes to core OCR processing logic

## Distribution Strategy
The new packaging enables multiple distribution methods:
- Direct execution with `uvx` from git repository
- Installation as a tool with `uv tool install`
- Traditional pip installation from source
- Future PyPI distribution potential

## Error Handling
Error handling and logging remain unchanged to maintain consistency with existing user expectations.

## Virtual Environment Management

### Current State
The project currently includes a `.venv` directory created with traditional Python virtual environment tools and pip for dependency management.

### Proposed Changes
With the conversion to uv-based dependency management:
- The existing `.venv` directory will be ignored in favor of uv's virtual environment management
- Development workflow will shift from `python -m venv .venv` and `pip install -r requirements.txt` to `uv venv` and `uv sync`
- The `.gitignore` file should be updated to reflect uv-specific patterns if needed
- Both traditional and uv workflows should be documented to support developers with different preferences

### VSCode on Windows Compatibility
- uv-created virtual environments (typically in uv's global cache) must be properly recognized by VSCode on Windows
- Users may need to manually select the Python interpreter in VSCode after uv environment creation
- Documentation should include instructions for Windows VSCode users to locate and select uv-managed Python interpreters
- Verify that `uv python list` and `uv venv` work correctly on Windows environments
- Consider that uv may create virtual environments in a different location than the project directory on Windows

### Compatibility Considerations
- The project will maintain compatibility with both systems during transition
- Users can continue using existing `.venv` if they prefer the traditional approach
- New users will be guided toward uv-based workflows in documentation
- The existing `.venv` directory should be preserved during the transition to avoid breaking existing setups
- A migration path should be provided for users wanting to transition from existing `.venv` to uv environments
- Both the existing project-local `.venv` and uv's global cache environments should function properly

### Transition Strategy for Existing .venv
- Existing `.venv` directories will continue to work with the new pyproject.toml (can be recreated with `python -m venv .venv` and `pip install -e .`)
- Documentation should provide a clear migration path: backup current `.venv`, remove old `.venv`, use `uv venv` to create new environment
- The project should function with both approaches during a transition period to allow users to migrate at their own pace