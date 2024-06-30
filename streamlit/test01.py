# streamlit run your_script.py [-- script args]

import streamlit as st

import random
import base64
import pandas as pd
import numpy as np

st.title("test01.py")

username = st.text_input("Enter a Username", "Bob")
password = st.text_input("Enter a password", type="password")

st.write(f"Username: {username}")
st.write(f"Password: {password}")

# -- DF1

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')

# -- DF2

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))


# -- DF3 

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
