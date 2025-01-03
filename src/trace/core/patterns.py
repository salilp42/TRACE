class MLPatterns:
    """Enhanced ML-related patterns for detection."""
    
    TRANSFORMS = {
        "normalize", "scale", "standardize", "fit_transform", 
        "fit", "transform", "encode", "preprocess"
    }
    
    DATA_OPS = {
        "merge", "join", "concat", "append", "combine", 
        "group", "aggregate", "reshape"
    }
    
    TIME_PATTERNS = {
        "date", "time", "timestamp", "datetime", "period",
        "year", "month", "day", "hour", "minute"
    }
    
    FOLD_KEYWORDS = {"train", "test", "valid", "eval", "predict", "split"}
    
    PARTICIPANT_PATTERNS = {"patient", "participant", "subject", "id", "case"}
    
    DRIFT_INDICATORS = {
        "distribution", "shift", "drift", "concept_drift",
        "covariate_shift", "domain_adaptation"
    }
