import streamlit as st
import difflib

# Array of items
items = ["US", "UK", "Canada", "Australia", "Germany", "France", "Japan", "China", "India", "Brazil"]

# Streamlit UI
st.title("Closest Match Finder")

user_input = st.text_input("Type a country:", "")

if user_input:
    closest_match = difflib.get_close_matches(user_input, items)
    if closest_match:
        st.write(f"Closest match: {closest_match[0]}")
    else:
        st.write("No close match found.")
