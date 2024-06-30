# streamlit run your_script.py [-- script args]

import streamlit as st

import random
import base64
import pandas as pd
import numpy as np

st.title("test04.py")


st.markdown("Hello **Markdown**")
st.header("Hello Header")
st.title("Hello Title")
st.subheader("Hello SubHeader")
st.caption("Hello caption")
st.code("a = 1234")
with st.echo():
    st.write("This text will be printed")
st.text("Hello text")
st.latex("\int a x^2 \,dx")
st.divider()