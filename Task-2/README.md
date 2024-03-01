# Closest Match Finder

This Streamlit app allows you to find the closest match to a target value in an array of items. It's useful for scenarios where you need to quickly find the closest match to a specific value, such as finding the closest country name or word in a list.

## Features

- Input a target value and an array of items.
- Finds the closest match to the target value in the array.
- Supports large arrays of items.

## Usage

1. Install the necessary dependencies using `pip install -r requirements.txt`.
2. Run the Streamlit app using `streamlit run app.py`.
3. Enter the target value and an array of items in the provided input fields.
4. The app will display the closest match to the target value in the array.

## Example

Target value: "India"
Array of items:
Copy code
Canada
Mexico
Brazil
Argentina
United Kingdom
United States
Germany
France
Italy
China
Japan
Australia
Russia
South Africa
Output: "The closest match to 'India' in the array is: 'China'"
## Libraries Used

- Streamlit: For building the web app interface.
- difflib: For finding the closest match to the target value in the array.

## About

This Streamlit app is created by [Your Name]. It's a simple tool designed to demonstrate how to find the closest match in an array of items using Python and Streamlit.
