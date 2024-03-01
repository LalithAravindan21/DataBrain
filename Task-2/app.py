import streamlit as st
import difflib

# Array of items
items = ["US", "UK", "Canada", "Australia", "Germany", "France", "Japan", "China", "India", "Brazil"]

# Streamlit UI
st.title("Closest Match Finder")

user_input = st.text_input("Type a country:", "")

if user_input:
    closest_matches = difflib.get_close_matches(user_input, items, n=2)
    closest_matches = [match for match in closest_matches if match != user_input]
    if closest_matches:
        st.write(f"Closest match: {closest_matches[0]}")
    else:
        st.write("No close match found.")
