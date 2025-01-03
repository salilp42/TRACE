import pytest
from trace.core.detector import LeakageDetector

# Test cases for LeakageDetector

def test_leakage_detector_initialization():
    detector = LeakageDetector()
    assert detector.flows == []
    assert detector.participant_vars == set()
    assert detector.fold_vars == set()
    assert detector.time_vars == set()
    assert detector.current_function is None
    assert detector.current_file == ""
