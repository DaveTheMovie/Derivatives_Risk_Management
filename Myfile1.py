# Import the Streamlit library
import streamlit as st

# Create a title for your app
st.title('Simple Streamlit App')

# Create a text element
st.write('This is a simple app that squares a number.')

# Ask the user to input a number
number = st.number_input('Insert a number')

# Square the number and display the result
result = number * number
st.write('The square of the number is: ', result)
