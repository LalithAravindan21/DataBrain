import streamlit as st
import PyPDF2

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
    # Convert question and text to lowercase for case-insensitive matching
    question = question.lower()
    text = text.lower()

    # Search for question keywords in the text
    if question in text:
        # If question keywords found, return the relevant part of the text
        return text[text.find(question):]

    # If question keywords not found, return None
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
