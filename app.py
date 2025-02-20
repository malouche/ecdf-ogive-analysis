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

def main():
    st.title('ECDF and Ogive Analysis')
    st.markdown("""
        Analyze and visualize data using Empirical Cumulative Distribution Functions (ECDF) 
        and Ogive curves. This tool helps understand the distribution of your data without 
        making strong assumptions about the underlying distribution.
    """)
    
    tabs = st.tabs(['ECDF Analysis', 'Ogive Analysis', 'Help', 'About'])
    
    with tabs[0]:
        st.header('ECDF Analysis')
        st.markdown("""
            The Empirical Cumulative Distribution Function (ECDF) is obtained by assigning 
            probability 1/n to each data point. For a point x, F_n(x) is the proportion of 
            observations less than or equal to x.
        """)
        
        with st.expander("📊 About ECDF", expanded=True):
            st.markdown("""
                #### Key Properties:
                - Step function with jumps at each data point
                - Right-continuous
                - Takes values between 0 and 1
                - F_n(x) = (number of observations ≤ x) / n
                
                #### Input Requirements:
                1. **X values:** Your data points (must be in ascending order)
                2. **Frequencies:** Corresponding frequency for each x value (must be positive)
            """)
        
        n = st.number_input('Number of data points (n)', min_value=1, value=3, step=1)
        
        col1, col2 = st.columns(2)
        x_values = []
        y_values = []
        
        with col1:
            st.subheader("X Values")
            for i in range(n):
                x = st.number_input(f'X value {i+1}', 
                                  key=f'x_{i}', 
                                  format='%.2f',
                                  step=0.1)
                x_values.append(x)
        
        with col2:
            st.subheader("Frequencies")
            for i in range(n):
                y = st.number_input(f'Frequency {i+1}',
                                  min_value=0,
                                  value=1,
                                  step=1,
                                  key=f'y_{i}')
                y_values.append(y)
        
        if st.button('Generate ECDF Analysis'):
            if len(set(x_values)) != len(x_values):
                st.error('❌ Error: X values must be unique!')
                return
            
            if not all(y > 0 for y in y_values):
                st.error('❌ Error: All frequencies must be positive!')
                return
            
            x = np.array(x_values)
            y = np.array(y_values)
            
            if not np.all(np.diff(x) > 0):
                st.error('❌ Error: X values must be in ascending order!')
                return
            
            st.markdown("### Results")
            
            results_df = pd.DataFrame({
                'X': x,
                'Frequency': y,
                'F(x)': calculate_ecdf(x, y)[1]
            })
            st.dataframe(results_df.style.format({
                'X': '{:.2f}',
                'F(x)': '{:.3f}'
            }))
            
            st.markdown("### ECDF Function")
            st.latex(ecdf_math_function(x, y))
            
            st.plotly_chart(plot_ecdf(x, y), use_container_width=True)
    
    with tabs[1]:
        st.header('Ogive Analysis')
        st.markdown("""
            For grouped data, the Ogive provides a continuous approximation of the cumulative 
            distribution using linear interpolation between group boundaries.
        """)
        
        with st.expander("📊 About Ogive", expanded=True):
            st.markdown("""
                #### Mathematical Definition:
                For grouped data in intervals [c_{j-1}, c_j], the Ogive F_n(x) is:
                
                F_n(x) = ((c_j - x)/(c_j - c_{j-1}))F_n(c_{j-1}) + ((x - c_{j-1})/(c_j - c_{j-1}))F_n(c_j)
                
                where:
                - c_0 < c_1 < ... < c_k are the group boundaries
                - n_j is the number of observations between c_{j-1} and c_j
                - F_n(c_j) = (1/n)∑n_i up to j
            """)
        
        m = st.number_input('Number of group boundaries', min_value=2, value=4, step=1)
        
        col1, col2 = st.columns(2)
        groups_values = []
        freq_values = []
        
        with col1:
            st.subheader("Group Boundaries")
            for i in range(m):
                g = st.number_input(f'Boundary {i+1}',
                                  key=f'g_{i}',
                                  format='%.2f',
                                  step=0.1)
                groups_values.append(g)
        
        with col2:
            st.subheader("Class Frequencies")
            for i in range(m-1):
                f = st.number_input(f'Frequency for class {i+1}',
                                  min_value=0,
                                  value=1,
                                  step=1,
                                  key=f'f_{i}')
                freq_values.append(f)
        
        if st.button('Generate Ogive Analysis'):
            if len(set(groups_values)) != len(groups_values):
                st.error('❌ Error: Group boundaries must be unique!')
                return
            
            if not all(f > 0 for f in freq_values):
                st.error('❌ Error: All frequencies must be positive!')
                return
            
            groups = np.array(groups_values)
            frequencies = np.array(freq_values)
            
            if not np.all(np.diff(groups) > 0):
                st.error('❌ Error: Group boundaries must be in ascending order!')
                return
            
            st.markdown("### Results")
            
            results_df = pd.DataFrame({
                'Lower Boundary': groups[:-1],
                'Upper Boundary': groups[1:],
                'Frequency': frequencies,
                'Cumulative Proportion': calculate_ogive(groups, frequencies)[1:]
            })
            st.dataframe(results_df.style.format({
                'Lower Boundary': '{:.2f}',
                'Upper Boundary': '{:.2f}',
                'Cumulative Proportion': '{:.3f}'
            }))
            
            st.markdown("### Ogive Function")
            st.latex(ogive_math_function(groups, frequencies))
            
            st.plotly_chart(plot_ogive(groups, frequencies), use_container_width=True)
    
    with tabs[2]:
        st.header('Help & Documentation')
        st.markdown("""
            ### Data-Dependent Distributions
            
            This application focuses on models based on data-dependent distributions without 
            making strong assumptions about the underlying distribution.
            
            #### Key Assumptions:
            - Sample Size: n observations
            - Nature of Sample: Independent and identically distributed (i.i.d.)
            - Distribution Type: Continuous, but unspecified
            
            This represents a complete data situation.
            
            ### Example Data
            #### Discrete Data Example (Accident Data):
            ```
            Number of accidents | Number of drivers
            0                  | 81,714
            1                  | 11,306
            2                  | 1,618
            3                  | 250
            4                  | 40
            5 or more         | 7
            ```
            
            #### Grouped Data Example (Insurance Claims):
            ```
            Payment range      | Number of payments
            0 - 7,500         | 99
            7,500 - 17,500    | 42
            17,500 - 32,500   | 29
            32,500 - 67,500   | 28
            67,500 - 125,000  | 17
            125,000 - 300,000 | 9
            Over 300,000      | 3
            ```
        """)
    
    with tabs[3]:
        st.header('About')
        st.markdown("""
            ### Developer Information
            
            **Prof. Dhafer Malouche**  
            Professor of Statistics  
            Qatar University
            
            📧 Email: [dhafer.malouche@qu.edu.qa](mailto:dhafer.malouche@qu.edu.qa)
            
            This application implements empirical models for complete data analysis, 
            focusing on ECDF and Ogive visualizations based on statistical theory 
            and practice.
        """)

if __name__ == '__main__':
    main()