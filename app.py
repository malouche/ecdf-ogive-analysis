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

def main():
    local_css()
    st.title("ECDF and Ogive Analysis")
    
if __name__ == "__main__":
    main()