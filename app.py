# [Previous imports and functions remain the same...]

def main():
    # [Previous code remains the same until the expanders...]
    
    with tabs[0]:
        st.header('ECDF Analysis')
        st.markdown("""
            The Empirical Cumulative Distribution Function (ECDF) is obtained by assigning 
            probability 1/n to each data point.
        """)
        
        with st.expander("📊 About ECDF", expanded=True):
            st.markdown("#### Key Properties:")
            
            # ECDF definition in LaTeX
            st.latex(r'''
            F_n(x) = \frac{\text{number of observations} \leq x}{n}
            ''')
            
            st.markdown("""
                - Step function with jumps at each data point
                - Right-continuous
                - Takes values between 0 and 1
            """)
            
            st.markdown("#### Input Requirements:")
            st.markdown("""
                1. **X values:** Your data points (must be in ascending order)
                2. **Frequencies:** Corresponding frequency for each x value (must be positive)
            """)
    
    with tabs[1]:
        st.header('Ogive Analysis')
        st.markdown("""
            For grouped data, the Ogive provides a continuous approximation of the cumulative 
            distribution using linear interpolation between group boundaries.
        """)
        
        with st.expander("📊 About Ogive", expanded=True):
            st.markdown("#### Mathematical Definition:")
            st.markdown("For grouped data in intervals [c_{j-1}, c_j], the Ogive F_n(x) is:")
            
            # Ogive formula in LaTeX
            st.latex(r'''
            F_n(x) = \frac{c_j - x}{c_j - c_{j-1}}F_n(c_{j-1}) + \frac{x - c_{j-1}}{c_j - c_{j-1}}F_n(c_j)
            ''')
            
            st.markdown("where:")
            st.latex(r'''
            c_0 < c_1 < \cdots < c_k \text{ are the group boundaries}
            ''')
            st.latex(r'''
            n_j \text{ is the number of observations between } c_{j-1} \text{ and } c_j
            ''')
            st.latex(r'''
            F_n(c_j) = \frac{1}{n}\sum_{i=1}^j n_i
            ''')
            
    # [Rest of the code remains the same...]