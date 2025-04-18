import streamlit as st

# Set the title of the app
st.title("Fibonacci Sequence Generator")

# Input for the number of terms in the Fibonacci sequence
num_terms = st.number_input("Enter the number of terms:", min_value=1, value=10)

# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
    return sequence[:n]

# Button to generate the Fibonacci sequence
if st.button("Generate Fibonacci Sequence"):
    fib_sequence = fibonacci(num_terms)
    st.write(f"The first {num_terms} terms of the Fibonacci sequence are: {fib_sequence}")
