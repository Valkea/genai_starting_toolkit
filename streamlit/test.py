# streamlit run your_script.py [-- script args]

import streamlit as st

import random
import base64
import pandas as pd
import numpy as np

# -- Nav

pages = {
    "Your account" : [
        st.Page("test01.py", title="Dataframes examples"),
        st.Page("test02.py", title="Charts examples")
    ],
    "Resources" : [
        st.Page("test03.py", title="Audio / Images / Video ... examples"),
        st.Page("test04.py", title="Texts examples"),
        st.Page("test05.py", title="Chat example")
    ]
}

pg = st.navigation(pages)
pg.run()

st.title("test.py")

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://marketplace.canva.com/EAFCO6pfthY/1/0/1600w/canva-blue-green-watercolor-linktree-background-F2CyNS5sQdM.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()