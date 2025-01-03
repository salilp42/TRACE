import typer
from trace.core.detector import LeakageDetector
from trace.visualization.report import generate_html_report

app = typer.Typer()

@app.command()
def trace(path: str):
    """Main entry point for TRACE analysis."""
    # Implementation will go here
    pass

if __name__ == "__main__":
    app()
