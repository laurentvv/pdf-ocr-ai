# Tasks: Convert Project from pip to uv

## 1. Setup pyproject.toml
- [ ] Create `pyproject.toml` with project metadata
- [ ] Migrate dependencies from `requirements.txt`
- [ ] Define console script entry point

## 2. Package Structure Validation
- [ ] Ensure project structure supports proper packaging
- [ ] Verify command-line interface works as expected

## 3. Testing uv Installation Methods
- [ ] Test `uv sync` for local development
- [ ] Test `uvx` execution from git repository
- [ ] Test `uv tool install` from git repository

## 4. Backward Compatibility Verification
- [ ] Ensure existing `python pdf_ocr_lmstudio.py <input.pdf> <output.md>` still works
- [ ] Test all current functionality after changes

## 5. Documentation Update
- [ ] Update README.md with new installation and usage instructions
- [ ] Update README_FR.md with new installation and usage instructions (French version)
- [ ] Document both traditional and uv-based methods in both README files
- [ ] Add examples for uvx and uv tool install usage in both README files
- [ ] Include guidance on virtual environment management with uv vs traditional .venv in both README files
- [ ] Include specific instructions for VSCode users on Windows to select uv Python interpreter in both README files

## 6. Virtual Environment Configuration
- [ ] Update .gitignore if needed to reflect uv-specific patterns
- [ ] Document both traditional .venv and uv workflows for developers
- [ ] Include specific instructions for VSCode users on Windows to select uv Python interpreter
- [ ] Test uv virtual environment creation and VSCode interpreter selection on Windows
- [ ] Document migration path from existing .venv to uv environments
- [ ] Verify existing .venv continues to function after pyproject.toml changes