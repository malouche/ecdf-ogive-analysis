import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Configure the page
st.set_page_config(
    page_title="ECDF and Ogive Analysis",
    layout="wide"
)

def calculate_ecdf(x, y):
    """Calculate ECDF values for points"""
    x = np.array(x)
    y = np.array(y)
    # Sort points
    sort_idx = np.argsort(x)
    x = x[sort_idx]
    y = y[sort_idx]
    
    # Calculate cumulative probabilities
    cum_y = np.cumsum(y)
    n = sum(y)
    cum_probs = cum_y / n
    
    return x, cum_probs

def plot_ecdf(x, y):
    """Plot ECDF as a proper step function"""
    x_sorted, cum_probs = calculate_ecdf(x, y)
    
    # Create steps for plotting
    x_steps = np.repeat(x_sorted, 2)[1:]
    x_steps = np.insert(x_steps, 0, x_sorted[0])
    x_steps = np.append(x_steps, x_sorted[-1])
    
    y_steps = np.repeat(cum_probs, 2)[:-1]
    y_steps = np.insert(y_steps, 0, 0)  # Start at 0
    
    fig = go.Figure()
    
    # Add main ECDF step function
    fig.add_trace(go.Scatter(
        x=x_steps,
        y=y_steps,
        mode='lines',
        name='ECDF',
        line=dict(color='#2C3E50', width=2)
    ))
    
    # Add points at the jumps
    fig.add_trace(go.Scatter(
        x=x_sorted,
        y=cum_probs,
        mode='markers',
        name='Jump points',
        marker=dict(color='#2C3E50', size=8)
    ))
    
    fig.update_layout(
        title={
            'text': 'Empirical Cumulative Distribution Function (ECDF)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='x',
        yaxis_title='F_n(x)',
        yaxis_range=[-0.05, 1.05],
        showlegend=False,
        template='plotly_white',
        hovermode='x'
    )
    
    return fig

def calculate_ogive(groups, frequencies):
    """Calculate Ogive values for grouped data"""
    cum_freq = np.cumsum(frequencies) / sum(frequencies)
    return np.append([0], cum_freq)  # Add 0 for the first boundary

def plot_ogive(groups, frequencies):
    """Plot Ogive as a continuous curve for grouped data"""
    cum_freq = calculate_ogive(groups, frequencies)
    
    fig = go.Figure()
    
    # Add connecting lines
    fig.add_trace(go.Scatter(
        x=groups,
        y=cum_freq,
        mode='lines+markers',
        name='Ogive',
        line=dict(color='#2C3E50', width=2),
        marker=dict(size=8, color='#2C3E50')
    ))
    
    fig.update_layout(
        title={
            'text': 'Ogive (Cumulative Frequency Polygon)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Group Boundaries',
        yaxis_title='Cumulative Proportion',
        yaxis_range=[-0.05, 1.05],
        template='plotly_white',
        hovermode='x'
    )
    
    return fig

def ecdf_math_function(x, y):
    """Generate LaTeX for ECDF function"""
    x_sorted, cum_probs = calculate_ecdf(x, y)
    ecdf_str = r"""
    F_n(x) = \begin{cases}
    """
    
    # First case for x < min
    ecdf_str += r"0, & x < " + f"{x_sorted[0]:.2f} \\\\"
    
    # Middle cases
    for i in range(len(x_sorted)-1):
        ecdf_str += f"{cum_probs[i]:.3f}, & {x_sorted[i]:.2f} \leq x < {x_sorted[i+1]:.2f} \\\\"
    
    # Last case for x ≥ max
    ecdf_str += f"1, & x \geq {x_sorted[-1]:.2f}"
    
    ecdf_str += r"""
    \end{cases}
    """
    return ecdf_str

def ogive_math_function(groups, frequencies):
    """Generate LaTeX for Ogive function"""
    cum_freq = calculate_ogive(groups, frequencies)[1:]  # Skip the initial 0
    ogive_str = r"""
    F_n(x) = \begin{cases}
    """
    
    # First case
    ogive_str += f"\\frac{{x}}{{{groups[0]}}} \\cdot {cum_freq[0]:.3f}, & 0 \leq x < {groups[0]} \\\\"
    
    # Middle cases
    for i in range(len(groups)-2):
        slope = (cum_freq[i+1] - cum_freq[i]) / (groups[i+1] - groups[i])
        intercept = cum_freq[i] - slope * groups[i]
        ogive_str += f"{slope:.6f}x + {intercept:.3f}, & {groups[i]} \leq x < {groups[i+1]} \\\\"
    
    # Last case
    ogive_str += f"1, & x \geq {groups[-1]}"
    
    ogive_str += r"""
    \end{cases}
    """
    return ogive_str

[Rest of the app code with UI elements...]