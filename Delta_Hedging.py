import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes formula for call option
def black_scholes_call(S, K, T, r, v):
    d1 = (np.log(S / K) + (r + 0.5 * v**2) * T) / (v * np.sqrt(T))
    d2 = d1 - v * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# Delta of a call option
def delta_call(S, K, T, r, v):
    d1 = (np.log(S / K) + (r + 0.5 * v**2) * T) / (v * np.sqrt(T))
    delta = norm.cdf(d1)
    return delta

# Function to plot the option values and tangent lines
def plot_option(S, K, T, r, v, tangent_lines, ax):
    S_values = np.linspace(50, 150, 100)
    call_prices = [black_scholes_call(s, K, T, r, v) for s in S_values]
    ax.plot(S_values, call_prices, label='Call Option Value')
    ax.axvline(x=S, color='gray', linestyle='--', label='Current S')

    # Plot all previous tangent lines
    for line in tangent_lines:
        intercept = line['intercept']  # Adjusted intercept
        slope = line['slope']
        tangent_prices = slope * (S_values - line['S']) + intercept
        ax.plot(S_values, tangent_prices, linestyle='--', label=f'Tangent at S={line["S"]:.2f}')

    ax.set_xlabel('Stock Price (S)')
    ax.set_ylabel('Option Price')
    ax.legend()


st.title('Delta Hedging Simulation')

# Sidebar inputs
S = st.sidebar.number_input('Stock Price (S)', min_value=50.0, max_value=150.0, value=100.0, step=1.0)
K = st.sidebar.number_input('Strike Price (K)', min_value=50.0, max_value=150.0, value=100.0, step=1.0)
T = st.sidebar.number_input('Time to Expiry (T)', min_value=0.1, max_value=5.0, value=1.0, step=0.1)
r = st.sidebar.number_input('Risk-free Rate (r)', min_value=-0.1, max_value=0.1, value=0.0, step=0.01)
v = st.sidebar.number_input('Volatility (v)', min_value=0.01, max_value=1.0, value=0.16, step=0.01)
mu = st.sidebar.number_input('Mean of dS (mu)', min_value=-20.0, max_value=20.0, value=0.0, step=0.1)
sigma = st.sidebar.number_input('SD of dS (sigma)', min_value=1.0, max_value=30.0, value=10.0, step=0.1)

if 'S_current' not in st.session_state:
    st.session_state.S_current = S
if 'profit_history' not in st.session_state:
    st.session_state.profit_history = []
if 'tangent_lines' not in st.session_state:
    st.session_state.tangent_lines = []

# Move button
if st.button('Move'):
    dS_random = np.random.normal(mu, sigma)
    st.session_state.S_current += dS_random
    profit = black_scholes_call(st.session_state.S_current, K, T, r, v) - \
             delta_call(st.session_state.S_current, K, T, r, v) * dS_random
    st.session_state.profit_history.append(profit)
    
    # Store tangent line data
    current_price = black_scholes_call(st.session_state.S_current, K, T, r, v)
    current_delta = delta_call(st.session_state.S_current, K, T, r, v)
    intercept = current_price - current_delta * st.session_state.S_current
    st.session_state.tangent_lines.append({'S': st.session_state.S_current, 'slope': current_delta, 'intercept': intercept})

# Display profits
st.write("Profit History:")
for i, p in enumerate(st.session_state.profit_history, 1):
    st.write(f"Move {i}: {p:.2f}")

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
plot_option(st.session_state.S_current, K, T, r, v, st.session_state.tangent_lines, ax)
st.pyplot(fig)
