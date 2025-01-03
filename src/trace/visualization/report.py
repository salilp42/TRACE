from jinja2 import Environment, PackageLoader
from datetime import datetime
from trace.core.detector import LeakageDetector
from trace.core.types import LeakageIssue

def generate_html_report(issues: List[LeakageIssue], detector: LeakageDetector) -> None:
    """Generate comprehensive HTML report."""
    env = Environment(loader=PackageLoader('trace', 'templates'))
    template = env.get_template('report.html')
    
    # Prepare report data
    report_data = {
        'timestamp': datetime.now().isoformat(),
        'issues': issues,
        'summary': {
            'total_issues': len(issues),
            'high_severity': len([i for i in issues if i.severity == Severity.HIGH]),
            'medium_severity': len([i for i in issues if i.severity == Severity.MEDIUM]),
            'low_severity': len([i for i in issues if i.severity == Severity.LOW])
        },
        'graph_stats': {
            'nodes': len(detector.graph.nodes()),
            'edges': len(detector.graph.edges()),
            'connected_components': nx.number_connected_components(detector.graph)
        }
    }
    
    # Generate HTML
    html_content = template.render(**report_data)
    with open('trace_report.html', 'w') as f:
        f.write(html_content)
