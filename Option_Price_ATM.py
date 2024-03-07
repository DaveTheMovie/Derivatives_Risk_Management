import streamlit as st
import random

# Lists of possible annual volatilities, times, and notionals
annualVols = [8, 16, 24, 32]
times = [.25,1,4]
notionals = [100, 200, 300, 400, 500]

def calculate_option_value(notional, time, annualVol):
    value = notional * (time ** 0.5) * annualVol / 100 * 0.4
    # st.write('Option Value:', value)  # For debugging
    return value

def reset_and_rerun():
    # Randomly choose new values for notional, time, and annualVol
    new_notional = random.choice(notionals)
    new_time = random.choice(times)
    new_annualVol = random.choice(annualVols)

    # Update the session state with these new values
    st.session_state['notional'] = new_notional
    st.session_state['time'] = new_time
    st.session_state['annualVol'] = new_annualVol

    # Rerun the app from the top
    st.experimental_rerun()

# Title and introduction
st.title('Derivatives Risk Management')
st.write('Option Valuation Trainer')

# Randomly choose values for notional, time, and annualVol
if 'notional' not in st.session_state or 'time' not in st.session_state or 'annualVol' not in st.session_state:
    st.session_state['notional'] = random.choice(notionals)
    st.session_state['time'] = random.choice(times)
    st.session_state['annualVol'] = random.choice(annualVols)

# Display the question and ask for the user's answer
question = f'''
A {st.session_state['time']} year, at the money, call option has a volatility of {st.session_state['annualVol']}%.
The notional value is {st.session_state['notional']}MM.
What is the value of the call option?
'''
user_answer = st.text_input(question)

# Submit button logic
if st.button('Submit'):
    answer = calculate_option_value(st.session_state['notional'], st.session_state['time'], st.session_state['annualVol'])
    if abs(float(user_answer) - answer) < .01:  # Comparing user's answer with actual answer
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The correct answer is {answer:.2f}.")  # Displaying the correct answer formatted to 2 decimal places

if st.button('Try Another Question'):
    reset_and_rerun()
