import streamlit as st
import difflib

def find_nearest_country(user_input, items):
    similarities = {country: difflib.SequenceMatcher(None, user_input, country).ratio() for country in items}
    del similarities[user_input]  # Remove the user's country from the similarities
    nearest_country = max(similarities, key=similarities.get)
    return nearest_country, similarities[nearest_country]

def main():
    st.title("Nearest Country Finder")

    # Define your array of items (countries)
    countries = ["US", "UK", "Canada", "Australia", "France", "Germany", "Japan", "China", "India", "Brazil"]

    # Get user input: Select their country
    user_country = st.selectbox("Select your country:", countries)

    if user_country:
        # Find nearest country
        nearest, similarity = find_nearest_country(user_country, countries)

        # Display result
        st.write(f"The nearest country to {user_country} is {nearest} (Similarity: {similarity:.2f})")

if __name__ == "__main__":
    main()
