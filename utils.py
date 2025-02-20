import numpy as np
import plotly.graph_objects as go

def calculate_ecdf(x, y):
    n = sum(y)
    cum_probs = np.cumsum(y) / n
    return cum_probs

def calculate_ogive(groups, frequencies):
    return np.cumsum(frequencies) / sum(frequencies)

def plot_ecdf(x, y):
    cum_probs = calculate_ecdf(x, y)
    
    fig = go.Figure()
    
    # Add ECDF step function (right-continuous)
    x_steps = np.repeat(x, 2)[1:]
    x_steps = np.insert(x_steps, 0, x[0])
    y_steps = np.concatenate(([0], np.repeat(cum_probs, 2)[:-1]))
    
    fig.add_trace(go.Scatter(
        x=x_steps,
        y=y_steps,
        mode='lines',
        name='ECDF',
        line=dict(color='#2C3E50', width=2)
    ))
    
    fig.update_layout(
        title={
            'text': 'Empirical Cumulative Distribution Function (ECDF)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='X',
        yaxis_title='F(x)',
        yaxis_range=[0, 1.1],
        template='plotly_white',
        hovermode='x',
        margin=dict(t=60, b=60, l=60, r=60)
    )
    
    return fig

def plot_ogive(groups, frequencies):
    cum_freq = calculate_ogive(groups, frequencies)
    
    fig = go.Figure()
    
    # Add Ogive
    fig.add_trace(go.Scatter(
        x=np.repeat(groups, 2)[1:],
        y=np.concatenate(([0], np.repeat(cum_freq, 2)[:-1])),
        mode='lines+markers',
        name='Ogive',
        line=dict(color='#2C3E50', width=2),
        marker=dict(size=8, color='#2C3E50')
    ))
    
    fig.update_layout(
        title={
            'text': 'Ogive',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='X',
        yaxis_title='Cumulative Proportion',
        yaxis_range=[0, 1.1],
        template='plotly_white',
        hovermode='x',
        margin=dict(t=60, b=60, l=60, r=60)
    )
    
    return fig