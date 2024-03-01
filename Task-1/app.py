import streamlit as st
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
import os

# Function to read PDF file
def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    num_pages = pdf_reader.numPages
    text = ""
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text

# Function to extract keywords using NLTK
def extract_keywords(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    keywords = [word for word, pos in tagged if pos.startswith("NN") or pos.startswith("VB")]
    return keywords

# Main function
def main():
    st.title("PDF Question Answering")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        text = read_pdf(uploaded_file)
        st.write("## PDF Contents:")
        st.write(text)

        question = st.text_input("Ask a question about the PDF:")
        if question:
            st.write("### Question:", question)
            keywords = extract_keywords(question)
            matching_sentences = []
            for sentence in sent_tokenize(text):
                if all(keyword.lower() in sentence.lower() for keyword in keywords):
                    matching_sentences.append(sentence.strip())
            if matching_sentences:
                st.write("### Answer:")
                for matching_sentence in matching_sentences:
                    st.write(matching_sentence)
            else:
                st.write("Sorry, I couldn't find an answer to that question.")

# Download NLTK data files and set NLTK data path
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
nltk.data.path.append(nltk_data_path)
os.environ["NLTK_DATA"] = nltk_data_path

# Run the main function
if __name__ == "__main__":
    main()
