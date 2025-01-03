import networkx as nx
import plotly.graph_objects as go
from trace.core.detector import LeakageDetector

def generate_interactive_graph(detector: LeakageDetector, issues: List[LeakageIssue]) -> None:
    """Generate interactive Plotly visualization."""
    G = detector.graph
    pos = nx.spring_layout(G)
    
    # Create edge traces
    edge_x = []
    edge_y = []
    edge_colors = []
    
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        
        # Color edges with issues
        if any(i.source_function == edge[0] and i.target_function == edge[1] for i in issues):
            edge_colors.extend(['red'] * 3)
        else:
            edge_colors.extend(['gray'] * 3)
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(color=edge_colors, width=2),
        hoverinfo='none',
        mode='lines'
    )
    
    # Create node traces
    node_x = []
    node_y = []
    node_text = []
    node_colors = []
    
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(str(node))
        
        # Color nodes based on type
        if node in detector.fold_vars:
            node_colors.append('lightblue')
        elif node in detector.time_vars:
            node_colors.append('orange')
        else:
            node_colors.append('lightgray')
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=node_text,
        marker=dict(
            color=node_colors,
            size=20,
            line_width=2
        )
    )
    
    # Create figure
    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=go.Layout(
                       title='Data Flow Graph',
                       showlegend=False,
                       hovermode='closest',
                       margin=dict(b=20,l=5,r=5,t=40),
                       annotations=[],
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                   ))
    
    fig.write_html("data_flow.html")
