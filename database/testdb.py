import pdfplumber
import re
import sqlite3

# 1. Convert PDFs to Text using pdfplumber
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

pdf_path = "/workspaces/codespaces-jupyter/database/test.pdf"  # Replace with your PDF file path
extracted_text = extract_text_from_pdf(pdf_path)

# 2. Data Cleaning
def clean_text(text):
    # Remove headers and footers or any other unwanted text
    # Replace 'Some Regular Expression' with actual patterns you want to remove
    text = re.sub(r"Some Regular Expression", "", text)
    return text

cleaned_text = clean_text(extracted_text)

# 3. Data Structuring
data = {
  "documents": [
    {
      "title": "Document 1",
      "content": cleaned_text
    }
  ]
}

# 4. Store in Database
def create_database():
    conn = sqlite3.connect("documents.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS Documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

create_database()

def insert_document(title, content):
    conn = sqlite3.connect("documents.db")
    c = conn.cursor()
    c.execute("INSERT INTO Documents (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

# Example usage:
insert_document("Document 1", cleaned_text)
