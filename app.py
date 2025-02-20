[Previous code remains exactly the same until the Help tab section...]

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
        Department of Statistics  
        College of Arts and Sciences  
        Qatar University
        
        #### Contact Information
        📧 Email: [dhafer.malouche@qu.edu.qa](mailto:dhafer.malouche@qu.edu.qa)  
        🔗 Office: E104-23  
        📞 Phone: +974 4403-7845  
        
        #### Research Interests
        - Statistical Data Analysis
        - Empirical Models
        - Nonparametric Statistics
        - Data Science Applications
        
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

# [Rest of the code remains exactly the same]