import streamlit as st
import pandas as pd
import numpy as np

st.title('Our First Web-App with streamlit')

st.text('Analyze random data')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.write('Plot a line chart')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)