import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Configure the page
st.set_page_config(
    page_title="ECDF and Ogive Analysis",
    layout="wide"
)

[Previous CSS styles remain the same...]

def main():
    local_css()
    
    st.title('ECDF and Ogive Analysis')
    st.markdown("""
        This application helps you analyze and visualize cumulative distribution functions 
        using both ECDF (Empirical Cumulative Distribution Function) and Ogive approaches.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(['ECDF Analysis', 'Ogive Analysis', 'Help', 'About'])
    
    with tab1:
        [Previous ECDF Analysis code remains the same...]
    
    with tab2:
        [Previous Ogive Analysis code remains the same...]
    
    with tab3:
        st.header('Help & Documentation')
        
        st.subheader('ECDF (Empirical Cumulative Distribution Function)')
        st.markdown("""
            The Empirical Cumulative Distribution Function (ECDF) is a step function that increases by 1/n at each of the n data points. It's used to estimate the cumulative distribution function of a random variable.

            #### How to Calculate ECDF:
            1. **Sort the data** in ascending order: x₁, x₂, ..., xₙ
            2. **For each value x:**
               - Calculate F(x) = (number of observations ≤ x) / (total number of observations)
            
            #### Properties of ECDF:
            - It ranges from 0 to 1
            - It is a step function
            - It increases only at observed data points
            - It is right-continuous
            
            #### When to Use ECDF:
            - To visualize the distribution of your data
            - To compare different distributions
            - To identify percentiles and quantiles
            - To detect outliers or unusual patterns
        """)
        
        st.divider()
        
        st.subheader('Ogive')
        st.markdown("""
            An Ogive is a graphical representation of a cumulative frequency distribution for grouped data. It's created by plotting the upper boundaries of groups against cumulative frequencies or proportions.

            #### How to Calculate Ogive:
            1. **Organize data** into groups/classes
            2. **Calculate frequencies** for each group
            3. **Calculate cumulative frequencies**
            4. **Plot points** at the upper boundaries
            
            #### Properties of Ogive:
            - It is a continuous curve
            - It is always increasing (non-decreasing)
            - It connects cumulative frequencies at class boundaries
            - Final value represents total frequency
            
            #### When to Use Ogive:
            - To represent grouped data
            - To find median and quartiles graphically
            - To compare different datasets
            - To analyze trends in cumulative data
        """)
        
        st.divider()
        
        st.subheader('Using This Application')
        st.markdown("""
            #### For ECDF Analysis:
            1. Enter the number of data points
            2. Input x-values and their corresponding frequencies
            3. Click 'Generate ECDF Analysis' to see:
               - Data table with cumulative probabilities
               - Mathematical function representation
               - Visual plot of the ECDF
            
            #### For Ogive Analysis:
            1. Enter the number of group boundaries
            2. Input boundary values and class frequencies
            3. Click 'Generate Ogive Analysis' to see:
               - Data table with cumulative proportions
               - Mathematical function representation
               - Visual plot of the Ogive
        """)
    
    with tab4:
        st.header('About')
        
        st.markdown("""
            ### Developer Information
            
            **Prof. Dhafer Malouche**  
            Professor of Statistics  
            Qatar University
            
            #### Contact Information
            📧 Email: [dhafer.malouche@qu.edu.qa](mailto:dhafer.malouche@qu.edu.qa)
            
            #### About This Application
            This application was developed to help students and researchers analyze and visualize cumulative distribution functions using both ECDF and Ogive approaches. It provides an interactive interface for:
            
            - Calculating and visualizing ECDF
            - Analyzing grouped data using Ogive
            - Generating mathematical representations
            - Creating publication-quality plots
            
            #### Version Information
            - Current Version: 1.0.0
            - Last Updated: February 2025
            
            #### Acknowledgments
            Built with:
            - Streamlit
            - Python Scientific Stack (NumPy, Pandas)
            - Plotly for interactive visualizations
            
            #### Feedback and Support
            For questions, suggestions, or technical support, please contact me via email.
            """)

if __name__ == '__main__':
    main()