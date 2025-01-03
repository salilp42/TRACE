# TRACE: Type Resolution And Call-graph Extractor for ML Research

TRACE is a lightweight yet powerful tool that automatically detects data leakage in machine learning research. Born from personal experience with the frustrating and subtle ways data can leak between training and testing sets, TRACE does automatically what I found myself coding manually for each project.

## Why TRACE?

Machine learning pipelines are complex systems where subtle data leakage can silently compromise experimental validity. A single preprocessing step shared between train and test sets, or an accidentally leaked feature, can lead to over-optimistic results and unreproducible research.
TRACE automatically identifies five critical categories of issues:

Cross-validation Leakage

Detects information bleeding between training and testing sets
Identifies shared preprocessing steps across data splits
Flags accidental data reuse in validation procedures


Preprocessing Contamination

Catches global normalization that spans train/test boundaries
Identifies shared feature transformations
Detects statistical leakage in preprocessing steps


Temporal Split Issues

Identifies future data influencing past predictions
Detects time-based split violations
Catches chronological inconsistencies in time series analysis


Data Imbalance Problems

Reports significant class distribution skews
Identifies potentially unreliable validation splits
Flags sampling issues that could affect model evaluation


Feature Leakage Risks

Detects indirect information leaks through feature engineering
Identifies target leakage in feature creation
Catches unintended correlations between features and splits


## Quick Start
```bash
pip install trace-ml
```

### Basic analysis
```bash
trace /path/to/project
```

### Generate interactive visualization
```bash
trace /path/to/project --graph
```

### Generate detailed HTML report
```bash
trace /path/to/project --output html
```

## Real-World Example
Consider this common scenario in medical ML research:
```python
def preprocess_patient_data(data):
    # Global normalization - potential leakage!
    normalized = normalize(data)
    return normalized

def train_model(train_data, test_data):
    # Cross-fold contamination risk
    processed_train = preprocess_patient_data(train_data)
    processed_test = preprocess_patient_data(test_data)
```
TRACE automatically detects this issue:
```bash
$ trace ./
 Found potential data leakage:
  HIGH: Cross-fold contamination in train_model
  - Shared preprocessing between train and test sets
  - File: train.py, Line: 12
```

## Key Features
1. **Intelligent Detection**  
   - AST-based analysis of Python codebases  
   - Pattern recognition for common ML operations  
   - Detection of subtle cross-validation issues

2. **Interactive Visualization**  
   - Dynamic data flow graphs using Plotly  
   - Clickable nodes showing detailed information  
   - Visual identification of problematic patterns

3. **Comprehensive Reporting**  
   - Detailed HTML reports  
   - Severity-based issue categorization  
   - Actionable recommendations

4. **Performance**  
   - Parallel processing for large codebases  
   - Caching for rapid re-analysis  
   - Minimal overhead

## Use Cases
- **Research Validation**  
   ```bash
   trace ./research_code --output html
   ```  
   Generates a comprehensive report for paper submission.

- **CI/CD Integration**  
   ```bash
   trace ./src --severity high
   ```  
   Catches critical issues in automated testing.

## Advanced Usage
### Custom Pattern Detection
```python
from trace.patterns import MLPatterns

# Add domain-specific patterns
MLPatterns.TRANSFORMS.update({
    "custom_normalize",
    "domain_transform"
})
```

### Severity Filtering
```bash
trace ./ --severity high
trace ./ --severity medium --output json
```

### Interactive Visualization
```bash
trace ./ --graph
# Opens interactive Plotly visualization in browser
```

## Contributing
Contributions are welcome! Please read our Contributing Guide for details on our code of conduct and the process for submitting pull requests.

## Citation
If you use TRACE in your research, please cite:
```bibtex
@software{patel2024trace,
  title = {TRACE: Type Resolution And Call-graph Extractor for Machine Learning Research},
  author = {Patel, Salil},
  year = {2024},
  url = {https://github.com/salilpatel/trace}
}
```

## License
MIT License - see the LICENSE file for details.

## Author
Salil Patel
