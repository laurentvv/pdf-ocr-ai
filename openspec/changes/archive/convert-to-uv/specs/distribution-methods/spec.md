# Spec: Distribution and Execution Methods

## ADDED Requirements

### Requirement: uvx Execution Support
The project MUST be executable via `uvx --from git-repository` command format.

#### Scenario: Direct Execution from Git Repository
Given the project is properly configured with pyproject.toml and console scripts
When a user executes `uvx --from git+https://github.com/laurentvv/pdf-to-md-ocr pdf-ocr-lmstudio <input.pdf> <output.md>`
Then the tool executes without requiring local installation

### Requirement: uv Tool Installation Support
The project MUST be installable via `uv tool install` command from a git repository.

#### Scenario: Tool Installation from Git Repository
Given the project is properly configured with pyproject.toml and console scripts
When a user executes `uv tool install git+https://github.com/laurentvv/pdf-to-md-ocr`
Then the tool is installed globally and accessible via command line

### Requirement: Installation Method Documentation
The project README MUST document both traditional and uv-based installation and execution methods.

#### Scenario: User-Friendly Documentation
Given updated documentation with uv installation instructions
When a user reads the README
Then they can understand and use both traditional and uv-based methods