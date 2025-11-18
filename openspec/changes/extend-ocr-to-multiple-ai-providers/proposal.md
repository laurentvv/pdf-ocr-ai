# Change Proposal: Extend OCR to Multiple AI Providers with Project Renaming

## Change ID
`extend-ocr-to-multiple-ai-providers`

## Overview
The project currently supports only LM Studio as an AI provider for OCR processing. This proposal adds support for Ollama and llama.cpp to provide users with multiple options for running local AI models, increasing flexibility and compatibility across different environments and use cases. Additionally, the project will be renamed to reflect its multi-provider nature rather than being tied to a specific provider name.

## Context
- Current implementation is locked to LM Studio with hard-coded API endpoint at `http://localhost:1234/v1`
- Users may prefer different local AI serving solutions based on their hardware, performance requirements, or availability
- Ollama provides an easy-to-use interface for running various open models
- llama.cpp offers lightweight inference with minimal dependencies
- Support for multiple providers increases the project's accessibility and adoption
- The current name `pdf-ocr-lmstudio` is misleading as it suggests LM Studio is the only supported provider

## Requirements
- Maintain backward compatibility with existing LM Studio functionality
- Implement provider selection via command-line argument
- Support the same set of vision models across all providers (including qwen/qwen3-vl-30b)
- Rename the project and CLI command to reflect multi-provider support (e.g., from `pdf-ocr-lmstudio` to `pdf-ocr-ai`)
- Preserve all existing functionality and output format
- Ensure consistent performance metrics and error handling across providers
- Update documentation to reflect the new name and multi-provider capabilities

## Success Criteria
- Users can switch between LM Studio, Ollama, and llama.cpp with a command-line flag
- All providers successfully process the same PDF input with comparable output quality
- Performance metrics remain consistent across providers
- No regression in existing LM Studio functionality
- Documentation updated to reflect new provider options and project name
- The tool is accessible via a new generic command name