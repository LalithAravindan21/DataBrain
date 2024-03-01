import streamlit as st
import difflib

def find_nearest_country(user_input, items):
    similarities = [(country, difflib.SequenceMatcher(None, user_input, country).ratio()) for country in items]
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[0][0]

def main():
    st.title("Array Display App")

    # Define your array of items
    items = ["US", "UK", "Canada", "Australia", "France", "Germany", "Japan", "China", "India", "Brazil"]

    # Get user input
    user_input = st.text_input("Type a country:")

    # Find nearest country
    nearest = find_nearest_country(user_input, items)

    # Display result
    st.write(f"Nearest country to '{user_input}': {nearest}")

if __name__ == "__main__":
    main()
