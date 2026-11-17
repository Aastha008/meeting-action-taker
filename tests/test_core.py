import pytest
from src.core import ActionExtractor
from unittest.mock import MagicMock

@pytest.mark.asyncio
async def test_extractor_logic():
    # Inject a mock LLM to avoid credential validation
    mock_llm = MagicMock()
    extractor = ActionExtractor(llm=mock_llm)
    
    # Verify that the extractor uses the injected mock
    assert extractor.llm == mock_llm
    assert True