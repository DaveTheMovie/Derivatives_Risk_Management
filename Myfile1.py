# Import the Streamlit library
import streamlit as st

def change(ds = .01, delta = 100, gamma = 0):
    d0 = delta
    d1 = delta + gamma/.01 * ds * 100
    dbar = (d0 + d1)/2
    dv = dbar * ds
    print(d0,d1,dbar,dv)
    return (delta + .5 * gamma/.01 * ds*100 ) * ds

# Create a title for your app
st.title('Derivatives Risk Management Trainer')

asdf = 1

# Create a text element
st.write(f'This is a simple app that squares a {asdf}.')

# Ask the user to input a number
number = st.number_input('Insert a number')

# Square the number and display the result
result = number * number
st.write('The square of the number is: ', result)
