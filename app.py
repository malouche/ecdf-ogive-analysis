import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Configure the page
st.set_page_config(
    page_title="ECDF and Ogive Analysis",
    layout="wide"
)

# Custom CSS styling
def local_css():
    st.markdown("""
        <style>
            .block-container {
                padding: 2rem;
            }
            
            div[data-testid="stExpander"] {
                background-color: #f8f9fa;
                border-left: 5px solid #4CAF50;
                padding: 1rem;
                margin: 1rem 0;
            }
            
            .stMarkdown {
                font-size: 1rem;
            }
            
            h1, h2, h3 {
                color: #2C3E50 !important;
                margin-bottom: 1rem;
            }
            
            div[data-testid="stDataFrame"] > div {
                border: 1px solid #ddd;
                border-radius: 0.5rem;
                padding: 1rem;
            }
            
            div[data-testid="stButton"] button {
                background-color: #4CAF50;
                color: white;
                width: 100%;
                padding: 0.75rem;
                margin: 1rem 0;
                border-radius: 0.5rem;
            }
            
            div[data-testid="stButton"] button:hover {
                background-color: #45a049;
            }
            
            .latex-container {
                background-color: #f8f9fa;
                padding: 2rem;
                border-radius: 0.5rem;
                margin: 1rem 0;
            }
            
            .number-input {
                width: 150px !important;
            }
            
            .stTabs [data-baseweb="tab-list"] {
                gap: 2rem;
            }
            
            .stTabs [data-baseweb="tab"] {
                height: 4rem;
            }
        </style>
    """, unsafe_allow_html=True)

# ECDF calculation functions
def calculate_ecdf(x, y):
    n = sum(y)
    cum_probs = np.cumsum(y) / n
    return cum_probs

def ecdf_math_function(x, y):
    cum_probs = calculate_ecdf(x, y)
    ecdf_str = r"\[ F(x) = \begin{cases} "
    
    for i in range(len(x)):
        if i == 0:
            ecdf_str += r"0 & \text{for } x < " + f"{x[i]:.2f}" + r" \\ "
        else:
            ecdf_str += f"{cum_probs[i-1]:.3f}" + r" & \text{for } " + f"{x[i-1]:.2f} \leq x < {x[i]:.2f}" + r" \\ "
    
    ecdf_str += f"1 & \\text{{for }} x \geq {x[-1]:.2f}" + r" \\ "
    ecdf_str += r"\end{cases} \]"
    return ecdf_str

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

# Ogive calculation functions
def calculate_ogive(groups, frequencies):
    return np.cumsum(frequencies) / sum(frequencies)

def ogive_math_function(groups, frequencies):
    cum_freq = calculate_ogive(groups, frequencies)
    ogive_str = r"\[ G(x) = \begin{cases} "
    
    for i in range(len(groups) - 1):
        if i == 0:
            ogive_str += r"0 & \text{for } x < " + f"{groups[i]:.2f}" + r" \\ "
        else:
            ogive_str += f"{cum_freq[i-1]:.3f}" + r" & \text{for } " + f"{groups[i-1]:.2f} \leq x < {groups[i]:.2f}" + r" \\ "
    
    ogive_str += f"1 & \\text{{for }} x \geq {groups[-1]:.2f}" + r" \\ "
    ogive_str += r"\end{cases} \]"
    return ogive_str

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

def main():
    local_css()
    
    st.title('ECDF and Ogive Analysis')
    st.markdown("""
        This application helps you analyze and visualize cumulative distribution functions 
        using both ECDF (Empirical Cumulative Distribution Function) and Ogive approaches.
    """)
    
    tab1, tab2 = st.tabs(['ECDF Analysis', 'Ogive Analysis'])
    
    with tab1:
        st.header('ECDF Analysis')
        
        with st.expander("📊 How to Input Your Data", expanded=True):
            st.markdown("""
                ### For ECDF analysis, you need:
                1. **X values:** Your data points on the x-axis
                2. **Frequencies:** The corresponding frequency for each x value
                
                **Important notes:**
                - Use numerical values only
                - Ensure x values are in ascending order
                - Each x value must have a corresponding frequency
                - Frequencies must be positive integers
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
            
            # Display data table
            results_df = pd.DataFrame({
                'X': x,
                'Frequency': y,
                'F(x)': calculate_ecdf(x, y)
            })
            st.dataframe(results_df.style.format({
                'X': '{:.2f}',
                'F(x)': '{:.3f}'
            }))
            
            # Display ECDF math function
            st.markdown("### ECDF Function")
            st.markdown('<div class="latex-container">', unsafe_allow_html=True)
            st.latex(ecdf_math_function(x, y))
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Plot ECDF
            st.plotly_chart(plot_ecdf(x, y), use_container_width=True)
    
    with tab2:
        st.header('Ogive Analysis')
        
        with st.expander("📊 How to Input Your Data", expanded=True):
            st.markdown("""
                ### For Ogive analysis, you need:
                1. **Group boundaries:** All class boundaries (including the upper bound of the last class)
                2. **Frequencies:** The frequency for each class
                
                **Important notes:**
                - Group boundaries must be in ascending order
                - Number of frequencies should be one less than the number of boundaries
                - Frequencies must be positive integers
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
            
            # Display data table
            results_df = pd.DataFrame({
                'Lower Boundary': groups[:-1],
                'Upper Boundary': groups[1:],
                'Frequency': frequencies,
                'Cumulative Proportion': calculate_ogive(groups, frequencies)
            })
            st.dataframe(results_df.style.format({
                'Lower Boundary': '{:.2f}',
                'Upper Boundary': '{:.2f}',
                'Cumulative Proportion': '{:.3f}'
            }))
            
            # Display Ogive math function
            st.markdown("### Ogive Function")
            st.markdown('<div class="latex-container">', unsafe_allow_html=True)
            st.latex(ogive_math_function(groups, frequencies))
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Plot Ogive
            st.plotly_chart(plot_ogive(groups, frequencies), use_container_width=True)

if __name__ == '__main__':
    main()