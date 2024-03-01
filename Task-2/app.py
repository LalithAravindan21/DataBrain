import streamlit as st
import difflib

def find_closest_match(target, items):
    closest_match = difflib.get_close_matches(target, items, n=1)
    if closest_match:
        return closest_match[0]
    else:
        return None

def main():
    st.title("Closest Match Finder")
    st.write("Enter a target value and an array of items, and I'll find the closest match in the array.")

    target = st.text_input("Enter the target value:")
    items_str = st.text_area("Enter the array of items (one item per line):")
    items = [x.strip() for x in items_str.split('\n') if x]

    if items:
        closest_match = find_closest_match(target, items)
        if closest_match:
            st.write(f"The closest match to '{target}' in the array is: '{closest_match}'")
        else:
            st.write("No match found.")

if __name__ == "__main__":
    main()
