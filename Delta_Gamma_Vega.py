# Import the Streamlit library
import streamlit as st
import random

deltas = [100,150,200,250,300,400,500,-100,-150,-200,-250,-300,-400,-500]
gammas = [100,150,200,250,300,400,500,-100,-150,-200,-250,-300,-400,-500]
vegas = [10,20,30,40,50]
changes_S = [1,2,3,4,5,-1,-2,-3,-4,-5]
changes_v = [.01,.02,.03,-.01,-.02,-.03]
S = 100

def change(ds = .01, S=100, delta = 100, gamma = 0, vega = 0, dv = 0):

    dP_delta = delta * ds/S
    dP_gamma = .5 * gamma * ds/S /.01 * ds/S
    dP_vega = vega * dv / .01

    dP = dP_delta + dP_gamma + dP_vega

    print(dP_delta,dP_gamma,dP_vega,dP)

    st.write('dP_Delta:', dP_delta, 'dP_gamma:', dP_gamma, 'dP_vega:', dP_vega, 'Change in Value:', dP)

    return dP

def reset_and_rerun():
    # Randomly choose new values for delta, gamma, and ds
    new_delta = random.choice(deltas)
    new_gamma = random.choice(gammas)
    new_vega = random.choice(vegas)
    new_ds = random.choice(changes_S)
    new_dv = random.choice(changes_v)

    # Update the session state with these new values
    st.session_state['delta'] = new_delta
    st.session_state['gamma'] = new_gamma
    st.session_state['ds'] = new_ds
    st.session_state['vega'] = new_vega
    st.session_state['dv'] = new_dv

    # Rerun the app from the top
    st.experimental_rerun()
    
# Title and introduction
st.title('Derivatives Risk Management')
st.write('Delta Gamma Vega Trainer')

# Randomly choose values for delta, gamma, and ds
delta = random.choice(deltas)
gamma = random.choice(gammas)
vega = random.choice(vegas)
ds = random.choice(changes_S)
dv = random.choice(changes_v)
S = 100

# Cache the values so they don't change on every rerun
if 'delta' not in st.session_state or 'gamma' not in st.session_state or 'ds' not in st.session_state or 'dv' not in st.session_state or 'vega' not in st.session_state:
    st.session_state['delta'] = delta
    st.session_state['gamma'] = gamma
    st.session_state['ds'] = ds
    st.session_state['dv'] = dv
    st.session_state['vega'] = vega

# Display the question and ask for the user's answer
question = f''' \n
What is the change in value given a \n
{st.session_state['ds']} percent change in the underlying \n
{st.session_state['dv']} percent point change in volatiltiy \n
delta of {st.session_state['delta']}m \n
gamma of {st.session_state['gamma']}m \n
vega of {st.session_state['vega']}m? \n
'''
user_answer = st.text_input(question)

# Submit button logic
if st.button('Submit'):
    answer = change(ds=st.session_state['ds'],S=S, delta=st.session_state['delta'], gamma=st.session_state['gamma'], vega=st.session_state['vega'], dv=st.session_state['dv'])
    if abs(float(user_answer) - answer) < .0001:  # Comparing user's answer with actual answer
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The correct answer is {answer:.4f}.")  # Displaying the correct answer formatted to 4 decimal places

if st.button('Try Another Question'):
    reset_and_rerun()
