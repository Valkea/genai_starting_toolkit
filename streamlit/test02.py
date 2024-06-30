# streamlit run your_script.py [-- script args]

import streamlit as st

import random
import base64
import pandas as pd
import numpy as np

st.title("test02.py")

col1, col2 = st.columns(2)

with col1:
    st.header("Area")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

with col2:
    st.header("Bar")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
    
col1, col2 = st.columns(2)

with col1:
    st.header("Line")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)