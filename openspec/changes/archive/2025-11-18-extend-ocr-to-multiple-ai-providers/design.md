# Design: Extend OCR to Multiple AI Providers with Project Renaming

## Architecture Overview

### Current Architecture
The current implementation has a monolithic approach where the `ocr_with_lmstudio` function is tightly coupled to LM Studio's API endpoint at `http://localhost:1234/v1`. The OpenAI client is initialized directly with these hard-coded values.

### Proposed Architecture
We'll implement a provider-based architecture with the following components:

```
Provider Interface
├── LMStudioProvider
├── OllamaProvider
├── LlamaCppProvider
└── ProviderFactory
```

The main `ocr_with_lmstudio` function will be refactored to accept a provider instance and become provider-agnostic.

### Provider Interface Definition
```python
class AIProvider:
    def __init__(self, base_url: str, api_key: str = None, **kwargs):
        pass

    def ocr_image(self, image_bytes: bytes, model: str, **kwargs) -> str:
        pass
```

### Provider Implementations

#### LMStudioProvider
- Base URL: `http://localhost:1234/v1` (configurable)
- API Key: Not required for local instances (backward compatibility maintained)
- Maintains current LM Studio behavior

#### OllamaProvider
- Base URL: `http://localhost:11434/v1` (configurable)
- API Key: Not required for local instances
- Uses Ollama's OpenAI-compatible endpoint
- Model naming: Direct mapping to Ollama models (e.g., "llava", "qwen2-vl")

#### LlamaCppProvider
- Base URL: `http://localhost:8080/v1` (configurable)
- API Key: Not required for local instances
- Uses llama.cpp's OpenAI-compatible endpoint
- Model naming: Direct mapping to loaded models

## Project Renaming Strategy

### File Renaming
- `pdf_ocr_lmstudio.py` → `pdf_ocr_ai.py` (or similar generic name)
- Update import statements and references within the codebase

### Package and CLI Renaming
- CLI command: `pdf-ocr-lmstudio` → `pdf-ocr-ai` (or similar generic name)
- Update pyproject.toml entry points
- Maintain backward compatibility if possible, or provide clear migration path

## Configuration and Command Line Interface

### New Command Line Options
- `--provider`: Select between "lm-studio", "ollama", "llama.cpp" (default: "lm-studio")
- `--provider-url`: Override default provider URL (optional)

### Backward Compatibility
- Default provider remains "lm-studio" to maintain existing behavior
- Existing command line arguments remain unchanged
- All functionality preserved with new provider selection capability
- Consider maintaining backward compatibility with old command name during transition period

## Error Handling and Validation
- Validate provider name at startup
- Validate API connectivity to selected provider
- Graceful fallback with informative error messages
- Provider-specific retry and timeout configurations

## Performance Considerations
- Each provider may have different performance characteristics
- Maintain consistent progress tracking and metrics across providers
- Allow for provider-specific optimization parameters