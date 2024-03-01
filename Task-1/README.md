PDF Question Answering
This is a simple application built with Streamlit and NLTK for extracting information and answering questions from PDF documents.

Overview
The application allows users to upload a PDF file and ask questions related to its contents. It extracts text from the PDF, processes it to identify keywords using NLTK, and then searches for matching sentences to form an answer to the user's question.

How to Use
Upload PDF: Click on the "Choose a PDF file" button and select the PDF document you want to analyze.

Ask a Question: After the PDF file is uploaded, enter your question in the provided text input box.

View Answer: The application will analyze the PDF content and attempt to find relevant sentences that answer your question. If a suitable answer is found, it will be displayed on the screen.

Installation
To run this application locally, follow these steps:

Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/pdf-question-answering.git
Navigate to the project directory:

bash
Copy code
cd pdf-question-answering
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Access the application in your web browser at http://localhost:8501.

Dependencies
Streamlit
NLTK
PyPDF2
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This application was created for educational purposes and is inspired by various tutorials and examples available online.
