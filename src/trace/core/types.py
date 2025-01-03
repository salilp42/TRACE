from dataclasses import dataclass, field
from typing import Dict, Set
from enum import Enum

class Severity(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class IssueType(str, Enum):
    CROSS_FOLD = "Cross-fold Leakage"
    TRANSFORM = "Transformation Leakage"
    DATA_DRIFT = "Data Drift Risk"
    TIME_SPLIT = "Temporal Split Issue"
    IMBALANCE = "Data Imbalance"

@dataclass
class DataFlow:
    """Represents a data flow between functions/modules."""
    source: str
    target: str
    variables: Set[str] = field(default_factory=set)
    file_path: str = ""
    line_number: int = 0
    metadata: Dict = field(default_factory=dict)

@dataclass
class LeakageIssue:
    """Represents a detected data leakage issue."""
    type: IssueType
    severity: Severity
    description: str
    file_path: str = ""
    line_number: int = 0
    source_function: str = ""
    target_function: str = ""
    metadata: Dict = field(default_factory=dict)
