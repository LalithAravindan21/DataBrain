import streamlit as st
from rapidfuzz import process

def find_closest_match(target, items):
    closest_match, _ = process.extractOne(target, items)
    return closest_match

def main():
    st.title("Closest Match Finder")
    st.write("Enter a target value and an array of items, and I'll find the closest match in the array.")

    target = st.text_input("Enter the target value:")
    items_str = st.text_input("Enter the array of items separated by commas:")
    items = [x.strip() for x in items_str.split(',') if x]

    if items:
        closest_match = find_closest_match(target, items)
        st.write(f"The closest match to '{target}' in the array is: '{closest_match}'")

if __name__ == "__main__":
    main()
