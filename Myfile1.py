# Import the Streamlit library
import streamlit as st
import random

deltas = [100,150,200,250,300,400,500]
gammas = [.1,.5,1,1.5,2,5,10,20]
changes = [1,2,3,4,5]

def change(ds = .01, delta = 100, gamma = 0):
    d0 = delta
    d1 = delta + gamma/.01 * ds * 100
    dbar = (d0 + d1)/2
    dv = dbar * ds
    print(d0,d1,dbar,dv)
    return (delta + .5 * gamma/.01 * ds*100 ) * ds

# Create a title for your app
st.title('Derivatives Risk Management')
st.title('Delta Gamma Trainer')

delta = random.choice(deltas)
gamma = random.choice(gammas)
ds = random.choice(changes)

# Ask the user for the sum
user_answer = st.number_input(f"What is the change in asset value given a {ds} percent change in the underlying and a delta of {delta} and a gamma of {gamma} ")

# Check if the user's answer is correct
answer = change(ds = ds/100, delta = delta, gamma = gamma)
if abs(float(user_answer) - answer) < .0001:
    st.write("Correct!")
else:
    st.write(f"Incorrect. The correct answer is {answer}.")
