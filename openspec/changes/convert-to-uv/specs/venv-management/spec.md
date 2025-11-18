# Spec: Virtual Environment Management

## MODIFIED Requirements

### Requirement: Virtual Environment Compatibility
The project MUST support both traditional virtual environments (.venv) and uv-based virtual environment management during the transition period.

#### Scenario: Backward Compatible Virtual Environment Usage
Given a project that has been converted to use pyproject.toml
When a user continues to use traditional .venv approach
Then the project functions correctly with existing virtual environment

#### Scenario: uv-based Virtual Environment Usage
Given a project that has been converted to use pyproject.toml
When a user creates virtual environment with `uv venv`
Then dependencies install correctly with `uv sync`

## ADDED Requirements

### Requirement: Developer Workflow Documentation
The project documentation MUST include guidance on both traditional and uv-based virtual environment workflows.

#### Scenario: Clear Developer Guidance
Given updated documentation with virtual environment guidance
When a developer reads the README
Then they understand both traditional .venv and uv venv approaches

### Requirement: VSCode on Windows Compatibility Documentation
The project documentation MUST include specific instructions for Windows VSCode users on how to work with uv-created virtual environments.

#### Scenario: VSCode Interpreter Recognition on Windows
Given a developer using VSCode on Windows with uv-managed virtual environments
When they need to select the Python interpreter for the project
Then documentation provides clear steps to locate and select the uv-managed Python environment