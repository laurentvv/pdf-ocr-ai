# Change Proposal: Extend OCR to Multiple AI Providers with Project Renaming

## Change ID
`extend-ocr-to-multiple-ai-providers`

## Why
The project currently supports only LM Studio as an AI provider for OCR processing. Users may prefer different local AI serving solutions based on their hardware, performance requirements, or availability. Ollama provides an easy-to-use interface for running various open models, and llama.cpp offers lightweight inference with minimal dependencies. Support for multiple providers increases the project's accessibility and adoption. Additionally, the current name `pdf-ocr-lmstudio` is misleading as it suggests LM Studio is the only supported provider.

## What Changes
- Current implementation is locked to LM Studio with hard-coded API endpoint at `http://localhost:1234/v1`
- Project will be renamed from `pdf-ocr-lmstudio` to `pdf-ocr-ai` to reflect multi-provider nature
- Command-line interface will be enhanced with `--provider` argument to select between LM Studio, Ollama, and llama.cpp
- Architecture will be refactored to support multiple AI providers through a common interface
- Documentation will be updated to reflect new multi-provider capabilities

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