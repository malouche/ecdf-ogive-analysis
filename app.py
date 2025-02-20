import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="ECDF and Ogive Analysis", layout="wide")

# Title
st.title("ECDF and Ogive Analysis")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["ECDF Analysis", "Ogive Analysis", "Help", "About"])

with tab1:
    st.header("ECDF Analysis")
    
    # About ECDF
    with st.expander("📊 About ECDF", expanded=True):
        st.markdown("#### Definition")
        st.latex(r'''
        \text{The empirical distribution is obtained by assigning probability } \frac{1}{n} \text{ to each data point.}
        ''')
        
        st.markdown("#### Key Properties")
        st.latex(r'''
        F_n(x) = \frac{\text{number of observations } \leq x}{n}
        ''')
        
        st.markdown("""
            Properties:
            - Step function with jumps at each data point
            - Right-continuous
            - Takes values between 0 and 1
        """)
    
    # ECDF Input
    n = st.number_input('Number of data points (n)', min_value=1, value=3)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("X Values")
        x_values = []
        for i in range(n):
            x = st.number_input(f"X{i+1}", value=float(i), key=f"x_{i}")
            x_values.append(x)
    
    with col2:
        st.subheader("Frequencies")
        freq_values = []
        for i in range(n):
            f = st.number_input(f"Freq{i+1}", value=1, min_value=1, key=f"f_{i}")
            freq_values.append(f)
    
    if st.button("Calculate ECDF"):
        x = np.array(x_values)
        y = np.array(freq_values)
        
        # Calculate ECDF
        cum_freq = np.cumsum(y)/sum(y)
        
        # Display results
        st.markdown("### Results")
        df = pd.DataFrame({
            'X': x,
            'Frequency': y,
            'Cumulative Frequency': cum_freq
        })
        st.dataframe(df)
        
        # Plot ECDF
        fig = go.Figure()
        
        # Create step function
        x_steps = []
        y_steps = [0]  # Start at 0
        
        for i in range(len(x)):
            x_steps.extend([x[i], x[i]])
            y_steps.extend([cum_freq[i], cum_freq[i]])
        
        fig.add_trace(go.Scatter(
            x=x_steps,
            y=y_steps,
            mode='lines',
            name='ECDF',
            line=dict(color='blue', width=2)
        ))
        
        fig.update_layout(
            title="ECDF Plot",
            xaxis_title="X",
            yaxis_title="Cumulative Frequency",
            yaxis_range=[0, 1.1]
        )
        
        st.plotly_chart(fig)

with tab2:
    st.header("Ogive Analysis")
    
    # About Ogive
    with st.expander("📊 About Ogive", expanded=True):
        st.markdown("#### Mathematical Definition")
        st.latex(r'''
        \text{For grouped data in intervals } [c_{j-1}, c_j] \text{, the Ogive } F_n(x) \text{ is:}
        ''')
        
        st.latex(r'''
        F_n(x) = \frac{c_j - x}{c_j - c_{j-1}}F_n(c_{j-1}) + \frac{x - c_{j-1}}{c_j - c_{j-1}}F_n(c_j)
        ''')
        
        st.latex(r'''
        \text{where:}
        ''')
        st.latex(r'''
        c_0 < c_1 < \cdots < c_k \text{ are the group boundaries}
        ''')
        st.latex(r'''
        n_j \text{ is the number of observations between } c_{j-1} \text{ and } c_j
        ''')
        st.latex(r'''
        F_n(c_j) = \frac{1}{n}\sum_{i=1}^j n_i
        ''')
    
    # Ogive Input
    m = st.number_input("Number of group boundaries", min_value=2, value=4)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Group Boundaries")
        boundaries = []
        for i in range(m):
            b = st.number_input(f"Boundary {i+1}", value=float(i), key=f"b_{i}")
            boundaries.append(b)
    
    with col2:
        st.subheader("Frequencies")
        ogive_freqs = []
        for i in range(m-1):
            f = st.number_input(f"Frequency {i+1}", value=1, min_value=1, key=f"of_{i}")
            ogive_freqs.append(f)
    
    if st.button("Calculate Ogive"):
        boundaries = np.array(boundaries)
        freqs = np.array(ogive_freqs)
        cum_freq = np.cumsum(freqs)/sum(freqs)
        
        # Display results
        st.markdown("### Results")
        df = pd.DataFrame({
            'Lower Bound': boundaries[:-1],
            'Upper Bound': boundaries[1:],
            'Frequency': freqs,
            'Cumulative Proportion': cum_freq
        })
        st.dataframe(df)
        
        # Plot Ogive
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=boundaries[1:],
            y=cum_freq,
            mode='lines+markers',
            line=dict(color='blue', width=2)
        ))
        
        fig.update_layout(
            title="Ogive Plot",
            xaxis_title="Group Boundary",
            yaxis_title="Cumulative Proportion",
            yaxis_range=[0, 1.1]
        )
        
        st.plotly_chart(fig)

with tab3:
    st.header("Help & Documentation")
    
    st.markdown("### Data-Dependent Distributions")
    st.markdown("""
        This application focuses on models based on data-dependent distributions without 
        making strong assumptions about the underlying distribution.
    """)
    
    st.markdown("### Key Assumptions")
    st.latex(r'''
    \begin{align*}
    & \bullet \text{ Sample Size: } n \text{ observations} \\
    & \bullet \text{ Nature of Sample: Independent and identically distributed (i.i.d.)} \\
    & \bullet \text{ Distribution Type: Continuous, but unspecified} \\
    & \bullet \text{ This represents a complete data situation}
    \end{align*}
    ''')
    
    st.markdown("### ECDF Details")
    st.markdown("""
        The Empirical Cumulative Distribution Function (ECDF) provides a non-parametric estimate 
        of the cumulative distribution function of a random variable. Key features:
        
        - **Non-parametric Nature**: Makes no assumptions about the underlying distribution
        - **Step Function**: Increases by 1/n at each data point
        - **Properties**: Right-continuous, ranges from 0 to 1
        - **Use Cases**: Distribution analysis, quantile estimation, goodness-of-fit tests
    """)
    
    st.markdown("### Ogive Details")
    st.markdown("""
        The Ogive provides a smooth approximation of the cumulative distribution for grouped data:
        
        - **Linear Interpolation**: Between group boundaries
        - **Continuous Function**: Unlike the step-function ECDF
        - **Use Cases**: Grouped data analysis, percentile estimation
        - **Advantages**: Visual smoothness, handles grouped data naturally
    """)
    
    st.markdown("### Example Data")
    st.markdown("#### Discrete Data Example (Accident Data):")
    st.markdown("""
        This dataset shows the distribution of accidents per driver over one year:
        - Most drivers (81,714) had no accidents
        - Only 7 drivers had 5 or more accidents
        - Shows typical right-skewed safety data pattern
    """)
    
    sample_data1 = pd.DataFrame({
        'Number of accidents': [0, 1, 2, 3, 4, '5 or more'],
        'Number of drivers': [81714, 11306, 1618, 250, 40, 7]
    })
    st.dataframe(sample_data1)
    
    st.markdown("#### Grouped Data Example (Insurance Claims):")
    st.markdown("""
        This dataset represents payment distribution from an insurance policy:
        - Grouped into intervals for easier analysis
        - Shows the common pattern in insurance claims
        - Demonstrates right-skewed financial data
    """)
    
    sample_data2 = pd.DataFrame({
        'Payment range': ['0 - 7,500', '7,500 - 17,500', '17,500 - 32,500', 
                        '32,500 - 67,500', '67,500 - 125,000', '125,000 - 300,000', 
                        'Over 300,000'],
        'Number of payments': [99, 42, 29, 28, 17, 9, 3]
    })
    st.dataframe(sample_data2)

with tab4:
    st.header("About")
    st.markdown("""
        ### Developer Information
        
        **Prof. Dhafer Malouche**  
        Professor of Statistics  
        College of Arts and Sciences  
        Qatar University
        
        #### Contact Information
        📧 Email: [dhafer.malouche@qu.edu.qa](mailto:dhafer.malouche@qu.edu.qa)
        
        #### About This Application
        This application implements empirical models for complete data analysis, focusing on:
        - ECDF visualization and analysis
        - Ogive curves for grouped data
        - Non-parametric distribution estimation
        - Interactive statistical visualization
        
        Developed as part of the Statistical Data Analysis course materials at Qatar University.
        
        #### Version Information
        - Current Version: 1.0.0
        - Last Updated: February 2025
        - Built with Streamlit and Python Scientific Stack
    """)