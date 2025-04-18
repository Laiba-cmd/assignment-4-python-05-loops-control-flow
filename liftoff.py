import streamlit as st
import time

# Set the title of the app
st.title("Liftoff!")

# Input for the user's goal
goal = st.text_input("Enter your goal:")

# Input for the countdown timer
countdown_time = st.number_input("Enter countdown time in seconds:", min_value=1, value=10)

# Button to start the countdown
if st.button("Start Countdown"):
    st.write(f"Starting countdown for: {goal}")
    for i in range(countdown_time, 0, -1):
        st.write(i)
        time.sleep(1)  # Wait for 1 second
    st.write("Liftoff! 🚀 Your goal is ready to launch!")
