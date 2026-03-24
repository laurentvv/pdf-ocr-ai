import sys
from unittest.mock import MagicMock

# Mock problematic dependencies before anything else loads
sys.modules['fitz'] = MagicMock()
sys.modules['tqdm'] = MagicMock()
sys.modules['openai'] = MagicMock()
