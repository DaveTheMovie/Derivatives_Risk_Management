import streamlit as st
import random

# Lists of possible notionals, DTLs, and annual volatilities
notionals = [150, 300, 450, 600, 750]
dtls = [5, 10, 15]
annualVols = [8, 16, 24, 32]

def calculate_haircut(notional, dtl, annualVol):
    adv = notional / dtl
    haircut = dtl / 5 * annualVol / 100 / 16 * notional
    st.write('Days to Liquidate:', dtl, 'Num std:', dtl/5,'Haircut:', haircut)
    return haircut

def reset_and_rerun():
    # Randomly choose new values for notional, dtl, and annualVol
    new_notional = random.choice(notionals)
    new_dtl = random.choice(dtls)
    new_annualVol = random.choice(annualVols)

    # Update the session state with these new values
    st.session_state['notional'] = new_notional
    st.session_state['dtl'] = new_dtl
    st.session_state['annualVol'] = new_annualVol

    # Rerun the app from the top
    st.experimental_rerun()

# Title and introduction
st.title('Derivatives Risk Management')
st.write('Haircut Estimation Trainer')

# Randomly choose values for notional, dtl, and annualVol
if 'notional' not in st.session_state or 'dtl' not in st.session_state or 'annualVol' not in st.session_state:
    st.session_state['notional'] = random.choice(notionals)
    st.session_state['dtl'] = random.choice(dtls)
    st.session_state['annualVol'] = random.choice(annualVols)

# Display the question and ask for the user's answer
adv = st.session_state['notional'] / st.session_state['dtl']
question = f'''
For a block trade ...
The notional value is {st.session_state['notional']}MM.
The average daily volume (ADV) is {adv}MM.
The annual volatility is {st.session_state['annualVol']}%.
What is the dollar value of the haircut?
'''
user_answer = st.text_input(question)

# Submit button logic
if st.button('Submit'):
    answer = calculate_haircut(st.session_state['notional'], st.session_state['dtl'], st.session_state['annualVol'])
    if abs(float(user_answer) - answer) < .01:  # Comparing user's answer with actual answer
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The correct answer is {answer:.2f}.")  # Displaying the correct answer formatted to 2 decimal places

if st.button('Try Another Question'):
    reset_and_rerun()
