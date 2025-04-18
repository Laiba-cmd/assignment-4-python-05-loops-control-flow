import streamlit as st
import random

# Set the title of the app
st.title("Wholesome Machine")

# Sample list of wholesome quotes
quotes = [
    "You are enough just as you are.",
    "Believe in yourself and all that you are.",
    "Every day may not be good, but there is something good in every day.",
    "You are capable of amazing things.",
    "Your only limit is your mind."
]

# Button to get a random quote
if st.button("Get Wholesome Quote"):
    quote = random.choice(quotes)
    st.write(quote)
