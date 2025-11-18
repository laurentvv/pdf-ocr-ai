# Spec: Package Structure for uv Distribution

## ADDED Requirements

### Requirement: pyproject.toml Configuration
The project MUST include a pyproject.toml file that defines:
- Project metadata (name, version, description, authors)
- Dependencies matching current requirements.txt
- Console script entry point for command-line execution

#### Scenario: Valid pyproject.toml Creation
Given a project using requirements.txt
When pyproject.toml is created with proper metadata
Then uv tools can properly recognize and install the project

### Requirement: Console Script Entry Point
The project MUST define a console script entry point in pyproject.toml that enables command-line execution.

#### Scenario: Console Script Execution via uvx
Given a project with proper console script definition in pyproject.toml
When uvx is used to execute the project from a git repository
Then the command-line interface executes successfully

### Requirement: Dependency Migration
All dependencies from requirements.txt MUST be properly migrated to pyproject.toml in the [project.dependencies] section.

#### Scenario: Dependency Resolution
Given dependencies are defined in pyproject.toml
When uv resolves dependencies
Then all required packages are installed correctly

## MODIFIED Requirements

### Requirement: Backward Compatibility
After conversion to pyproject.toml, the project MUST maintain all existing command-line interface behaviors.

#### Scenario: Backward Compatible Execution
Given the project has been converted to use pyproject.toml
When the original command-line interface is used (python pdf_ocr_lmstudio.py <input.pdf> <output.md>)
Then the tool executes with identical behavior as before the conversion