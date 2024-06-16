import openai
import sqlite3

def fetch_document_by_id(doc_id):
    conn = sqlite3.connect("documents.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Documents WHERE id=?", (doc_id,))
    document = c.fetchone()
    conn.close()
    if document:
        return document[2]  # Returning content of the document
    else:
        return None

# Initialize OpenAI API
openai.api_key = "XXX"

# Fetch a document from your database
document_content = fetch_document_by_id(1)  # Replace 1 with the ID of the document you want to summarize

# Use GPT-3 to summarize the document
if document_content:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following document:\n{document_content}",
        max_tokens=50  # Limiting to 50 tokens for the summary
    )
    summary = response.choices[0].text.strip()
    print(f"Summary: {summary}")
else:
    print("Document not found")
