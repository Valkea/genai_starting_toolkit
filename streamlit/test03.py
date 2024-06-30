# streamlit run your_script.py [-- script args]

import streamlit as st

import random
import base64
import pandas as pd
import numpy as np

st.title("test03.py")

# -- Audio

st.audio("medias/test.mp3")
st.audio("medias/test.wav")


# -- Image

st.image("medias/demo_chat.png")

# -- Logo (in left or top menu)
st.logo("medias/demo_chat.png")

