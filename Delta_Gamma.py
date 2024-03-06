# Import the Streamlit library
import streamlit as st
import random

# Lists of possible deltas, gammas, and changes
deltas = [100, 150, 200, 250, 300, 400, 500]
gammas = [0.1, 0.5, 1, 1.5, 2, 5, 10, 20]
changes = [1, 2, 3, 4, 5]

# Function to calculate the change in value
def change(ds=0.01, delta=100, gamma=0):
    d0 = delta
    d1 = delta + gamma / 0.01 * ds * 100
    dbar = (d0 + d1) / 2
    dv = dbar * ds
    st.write('Initial Delta:', d0, 'Final Delta:', d1, 'Average Delta:', dbar, 'Change in Value:', dv)  # For debugging
    return (delta + 0.5 * gamma / 0.01 * ds * 100) * ds
    
def reset_and_rerun():
    # Randomly choose new values for delta, gamma, and ds
    new_delta = random.choice(deltas)
    new_gamma = random.choice(gammas)
    new_ds = random.choice(changes)

    # Update the session state with these new values
    st.session_state['delta'] = new_delta
    st.session_state['gamma'] = new_gamma
    st.session_state['ds'] = new_ds

    # Rerun the app from the top
    st.experimental_rerun()
    
# Title and introduction
st.title('Derivatives Risk Management')
st.write('Delta Gamma Trainer')

# Randomly choose values for delta, gamma, and ds
delta = random.choice(deltas)
gamma = random.choice(gammas)
ds = random.choice(changes)

# Cache the values so they don't change on every rerun
if 'delta' not in st.session_state or 'gamma' not in st.session_state or 'ds' not in st.session_state:
    st.session_state['delta'] = delta
    st.session_state['gamma'] = gamma
    st.session_state['ds'] = ds

# Display the question and ask for the user's answer
question = f"What is the change in value given a {st.session_state['ds']} percent change in the underlying and a delta of {st.session_state['delta']} and a gamma of {st.session_state['gamma']}?"
user_answer = st.text_input(question)

# Submit button logic
if st.button('Submit'):
    answer = change(ds=st.session_state['ds'] / 100, delta=st.session_state['delta'], gamma=st.session_state['gamma'])
    if abs(float(user_answer) - answer) < .0001:  # Comparing user's answer with actual answer
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The correct answer is {answer:.4f}.")  # Displaying the correct answer formatted to 4 decimal places

if st.button('Try Another Question'):
    reset_and_rerun()
