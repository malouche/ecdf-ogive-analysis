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
    st.write("Enter your data for ECDF analysis")
    
    # Input for number of points
    n = st.number_input("Number of points", min_value=1, value=3)
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    # Input for x values
    with col1:
        st.subheader("X Values")
        x_values = []
        for i in range(n):
            x = st.number_input(f"X{i+1}", value=float(i), key=f"x_{i}")
            x_values.append(x)
    
    # Input for frequencies
    with col2:
        st.subheader("Frequencies")
        freq_values = []
        for i in range(n):
            f = st.number_input(f"Freq{i+1}", value=1, min_value=1, key=f"f_{i}")
            freq_values.append(f)
    
    if st.button("Calculate ECDF"):
        x = np.array(x_values)
        y = np.array(freq_values)
        cum_freq = np.cumsum(y)/sum(y)
        
        # Display results
        df = pd.DataFrame({
            'X': x,
            'Frequency': y,
            'Cumulative Frequency': cum_freq
        })
        st.write("Results:")
        st.dataframe(df)
        
        # Plot ECDF
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=cum_freq, mode='lines+markers'))
        fig.update_layout(title="ECDF Plot",
                         xaxis_title="X",
                         yaxis_title="Cumulative Frequency")
        st.plotly_chart(fig)

with tab2:
    st.header("Ogive Analysis")
    st.write("Enter your data for Ogive analysis")
    
    # Input for number of groups
    m = st.number_input("Number of group boundaries", min_value=2, value=4)
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    # Input for boundaries
    with col1:
        st.subheader("Group Boundaries")
        boundaries = []
        for i in range(m):
            b = st.number_input(f"Boundary {i+1}", value=float(i), key=f"b_{i}")
            boundaries.append(b)
    
    # Input for frequencies
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
        df = pd.DataFrame({
            'Lower Bound': boundaries[:-1],
            'Upper Bound': boundaries[1:],
            'Frequency': freqs,
            'Cumulative Proportion': cum_freq
        })
        st.write("Results:")
        st.dataframe(df)
        
        # Plot Ogive
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=boundaries[1:], y=cum_freq, mode='lines+markers'))
        fig.update_layout(title="Ogive Plot",
                         xaxis_title="Group Boundary",
                         yaxis_title="Cumulative Proportion")
        st.plotly_chart(fig)

with tab3:
    st.header("Help")
    st.write("""
    ### ECDF (Empirical Cumulative Distribution Function)
    
    The ECDF shows the proportion of observations less than or equal to each value.
    
    ### Ogive
    
    The Ogive is a graphical display of cumulative frequencies for grouped data.
    """)

with tab4:
    st.header("About")
    st.write("""
    ### Developer Information
    
    **Prof. Dhafer Malouche**  
    Professor of Statistics  
    Qatar University
    
    Email: dhafer.malouche@qu.edu.qa
    """)