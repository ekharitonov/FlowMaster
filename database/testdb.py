# 1. Convert PDFs to Text using pdfplumber

import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

pdf_path = "example.pdf"  # Replace with your PDF file path
extracted_text = extract_text_from_pdf(pdf_path)

# 2. Data Cleaning

import re

def clean_text(text):
    # Remove headers and footers or any other unwanted text
    text = re.sub(r"Some Regular Expression", "", text)
    return text

cleaned_text = clean_text(extracted_text)

# 3. Data Cleaning

data = {
  "documents": [
    {
      "title": "Document 1",
      "content": cleaned_text
    }
  ]
}

# 4. Store in Database
## Create the SQLite database and tables
import sqlite3

def create_database():
    conn = sqlite3.connect("documents.db")
    c = conn.cursor()

    # Create the Documents table
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

## Insert data into this table
def insert_document(title, content):
    conn = sqlite3.connect("documents.db")
    c = conn.cursor()

    c.execute("INSERT INTO Documents (title, content) VALUES (?, ?)", (title, content))

    conn.commit()
    conn.close()

# Example usage:
# insert_document("Document 1", cleaned_text)
