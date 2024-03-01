import streamlit as st
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text.lower())
    filtered_text = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_text)

# Function to read PDF file
def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    num_pages = pdf_reader.numPages
    text = ""
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text

# Function to search for answers in PDF text based on user question
def search_question(text, question):
    # Preprocess text and question
    preprocessed_text = preprocess_text(text)
    preprocessed_question = preprocess_text(question)

    # Vectorize text and question
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([preprocessed_text, preprocessed_question])

    # Calculate cosine similarity between text and question
    similarity = cosine_similarity(tfidf_matrix)[0, 1]

    # If similarity is above a threshold, return the relevant part of the text
    if similarity > 0.2:
        return text
    else:
        return None

# Main function
def main():
    st.title("PDF Question Answering")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        text = read_pdf(uploaded_file)
        st.write("## PDF Contents:")
        st.write(text)

        question = st.text_input("Ask a question about the PDF:")
        if question:
            st.write("### Question:", question)
            answer = search_question(text, question)
            if answer:
                st.write("### Answer:")
                st.write(answer)
            else:
                st.write("Sorry, I couldn't find an answer to that question.")

# Run the main function
if __name__ == "__main__":
    main()
