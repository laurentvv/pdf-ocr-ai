# Tasks: Extend OCR to Multiple AI Providers with Project Renaming

## Implementation Tasks

1. **Refactor existing architecture to support multiple AI providers**
   - Abstract the AI client/communication layer
   - Create a provider interface/protocol
   - Implement LM Studio provider (current functionality)
   - Implement Ollama provider
   - Implement llama.cpp provider

2. **Implement command-line argument for provider selection**
   - Add `--provider` argument (default: "lm-studio")
   - Add `--provider-url` argument for custom endpoints (optional)
   - Validate provider input
   - Handle provider-specific configuration (no API key required for local providers)

3. **Update AI client initialization logic**
   - Modify `ocr_with_lmstudio` function to become provider-agnostic
   - Create provider factory based on selected provider
   - Implement error handling for provider-specific issues

4. **Implement Ollama provider integration**
   - Use OpenAI-compatible API at `http://localhost:11434/v1`
   - Handle Ollama-specific model naming conventions
   - Test with vision-capable models like llava or qwen2-vl

5. **Implement llama.cpp provider integration**
   - Use OpenAI-compatible API at `http://localhost:8080/v1` (or configurable)
   - Handle llama.cpp-specific model loading and inference parameters
   - Test with vision-capable models

6. **Project renaming implementation**
   - Rename the main Python file from `pdf_ocr_lmstudio.py` to a more generic name (e.g., `pdf_ocr_ai.py`)
   - Update package name in pyproject.toml
   - Update CLI entry point to be more generic
   - Update function names that reference LM Studio specifically

7. **Update documentation and user guides**
   - Update README with new provider options
   - Add provider-specific setup instructions
   - Include examples for each provider
   - Update project name references throughout documentation

8. **Testing and validation**
   - Create integration tests for each provider
   - Validate output consistency across providers
   - Performance benchmarking across providers
   - Error handling verification
   - Test the renamed command works properly

## Dependencies
- Task 1 must be completed before other provider implementations
- Task 2 is needed before testing different providers
- Task 6 (renaming) can happen in parallel with provider implementations

## Parallelizable Work
- Tasks 4 and 5 (Ollama and llama.cpp implementations) can be done in parallel after Task 1
- Documentation updates can happen concurrently with implementation