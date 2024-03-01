import streamlit as st
import difflib

def find_closest_match(user_input, items):
    closest_match = difflib.get_close_matches(user_input, items)
    if closest_match:
        return closest_match[0]
    else:
        return None

def main():
    st.title("Array Display App")

    # Define your array of items
    items = ["US", "UK", "Canada", "Australia", "France", "Germany", "Japan", "China", "India", "Brazil"]

    # Get user input
    user_input = st.text_input("Type a country:")

    # Find closest match
    closest = find_closest_match(user_input, items)

    # Display result
    if closest:
        st.write(f"Closest match: {closest}")
    else:
        st.write("No match found.")

if __name__ == "__main__":
    main()
