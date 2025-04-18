import streamlit as st

# Set the title of the app
st.title("Event Printer")

# Sample list of events
events = [
    "Event 1: Streamlit Workshop",
    "Event 2: Python Conference",
    "Event 3: Data Science Meetup",
    "Event 4: AI Symposium",
    "Event 5: Web Development Bootcamp"
]

# Display the events
st.write("Here are some upcoming events:")
for event in events:
    st.write(event)

# Button to refresh the events
if st.button("Refresh Events"):
    st.write("Events refreshed!")
