import streamlit as st
import difflib

def find_nearest_country(user_input, items):
    similarity_scores = {country: difflib.SequenceMatcher(None, user_input, country).ratio() for country in items}
    nearest_country = max(similarity_scores, key=similarity_scores.get)
    return nearest_country

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
