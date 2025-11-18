# Multi-Provider AI Integration and Project Renaming Specification

## Overview
This specification defines the integration of multiple AI providers (Ollama and llama.cpp) in addition to the existing LM Studio support for PDF OCR processing, along with renaming the project to reflect its multi-provider nature.

## ADDED Requirements

### Requirement: REQ-PROV-001: Provider Selection via CLI
The application SHALL support selecting an AI provider via command-line argument.

#### Scenario: User selects Ollama provider
Given a user has Ollama running with a vision model loaded
When the user runs `pdf-ocr-lmstudio input.pdf output.md --provider ollama --model llava`
Then the application connects to Ollama's API endpoint and processes the PDF using the llava model

### Requirement: REQ-PROV-002: Provider Configuration Override
The application SHALL allow overriding default provider endpoints via command-line options.

#### Scenario: User specifies custom provider URL
Given a user has Ollama running on a non-standard port
When the user runs `pdf-ocr-lmstudio input.pdf output.md --provider ollama --provider-url http://localhost:11435/v1`
Then the application connects to the specified URL instead of the default Ollama endpoint

### Requirement: REQ-PROV-003: Llama.cpp Provider Support
The application SHALL support llama.cpp as an AI provider option.

#### Scenario: User selects llama.cpp provider
Given a user has llama.cpp server running with a vision model loaded
When the user runs `pdf-ocr-lmstudio input.pdf output.md --provider llama.cpp --model qwen2-vl`
Then the application connects to llama.cpp's API endpoint and processes the PDF using the qwen2-vl model

### Requirement: REQ-PROV-004: Provider Abstraction Interface
The application SHALL implement a common interface for all AI providers to maintain consistent OCR functionality.

#### Scenario: OCR processing with different providers
Given any selected provider (LM Studio, Ollama, or llama.cpp)
When OCR processing is initiated for a PDF page
Then the same OCR prompt and image processing logic is applied regardless of provider
And the output format remains consistent across all providers

### Requirement: REQ-PROV-005: Project Name Renaming
The project SHALL be renamed to reflect its multi-provider functionality instead of being tied to a specific provider name.

#### Scenario: CLI command uses new name
When the user installs and runs the tool after renaming
Then the command name SHALL reflect the multi-provider nature (e.g., `pdf-ocr-ai` instead of `pdf-ocr-lmstudio`)
And all references in documentation SHALL use the new generic name

## MODIFIED Requirements

### Requirement: REQ-MAIN-003: Command-Line Interface Enhancement
The existing CLI SHALL be extended to support provider selection while maintaining all current functionality.

#### Scenario: Help text shows new options
When the user runs `pdf-ocr-lmstudio --help`
Then the help text includes information about the `--provider` option
And the help text shows available provider options (lm-studio, ollama, llama.cpp)
And the help text does NOT include unnecessary `--api-key` option for local providers

#### Scenario: Invalid provider handling
When the user runs `pdf-ocr-lmstudio input.pdf output.md --provider invalid-provider`
Then the application returns an error message indicating the provider is not supported
And the application exits with a non-zero status

## REMOVED Requirements

No existing requirements are removed, ensuring backward compatibility.