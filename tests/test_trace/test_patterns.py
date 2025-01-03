import pytest
from trace.core.patterns import MLPatterns

# Test cases for MLPatterns

def test_patterns():
    assert "normalize" in MLPatterns.TRANSFORMS
    assert "merge" in MLPatterns.DATA_OPS
    assert "date" in MLPatterns.TIME_PATTERNS
    assert "train" in MLPatterns.FOLD_KEYWORDS
    assert "patient" in MLPatterns.PARTICIPANT_PATTERNS
    assert "drift" in MLPatterns.DRIFT_INDICATORS
