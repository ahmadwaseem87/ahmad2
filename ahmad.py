import streamlit as st
import numpy as np
st.title("Hello World")
st.write("Welcome to my first streamlit application!")
st.button("Click Me!")
progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))
for i in range(100):
    # Update progress bar.
    progress_bar.progress(i)
    new_rows = np.random.randn(10, 2)
    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])
    # Append data to the chart.
    chart.add_rows(new_rows)
status_text.text('Done!')
st.balloons()

import streamlit as st
st.title("Hello World")
st.write("Welcome to my first streamlit application!")
st.sidebar.title("Food Survey :smile:")
yogurt = st.sidebar.multiselect("Which do you like the most?",
                                ("Vanilla Yogurt","Berry Yogurt","Greek Yogurt"))
breakfast = st.sidebar.multiselect("Which do you like the most?",
                                ("Toast","Coffee","Weet-bix"))
fruits = st.sidebar.multiselect("Which do you like the most?",
                                ("Strawberry","Raspberry","Cherry"))
st.write("{} is your favourite type of yogurt".format(', '.join(yogurt)))
st.write("{} is your favourite type breakfast".format(', '.join(breakfast)))
st.write("{} is your favourite type of fruit".format(', '.join(fruits)))










