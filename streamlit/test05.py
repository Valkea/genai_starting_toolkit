# streamlit run your_script.py [-- script args]

import streamlit as st

import random
import base64
import pandas as pd
import numpy as np

st.title("test05.py")

 
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        r = random.randint(1,3)
        st.write(f"random {r}")
        match r:
            case 1:
                st.bar_chart(np.random.randn(30, 3))
            case 2:
                st.audio("medias/test.mp3")
            case 3:
                st.image("medias/back01.png")

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})