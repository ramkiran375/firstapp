import streamlit as st

# Title and header
st.title("My First Streamlit App")
st.header("Simple Data Exploration App")

# Text input
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")

# Number input
number = st.number_input("Enter a number", min_value=0, max_value=100)
st.write(f"Squared Value: {number ** 2}")

# Display a dataframe
import pandas as pd
data = {
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
st.write("Here is a sample dataframe:")
st.dataframe(df)
