import streamlit as st

# Set the title of the app
st.title("Double It!")

# Input for the number to double
number = st.number_input("Enter a number:", value=1)

# Button to calculate the double
if st.button("Double It"):
    doubled_value = number * 2
    st.write(f"The double of {number} is {doubled_value}.")
