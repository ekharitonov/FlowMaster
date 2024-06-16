import openai
import sqlite3

# Initialize OpenAI API
openai.api_key = "XXX"

def fetch_document_by_id(doc_id):
    conn = sqlite3.connect("documents.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Documents WHERE id=?", (doc_id,))
    document = c.fetchone()
    conn.close()
    if document:
        return document[2]  # Assuming content is the third column in the table
    else:
        return None

# Fetch a document from your database
document_content = fetch_document_by_id(1)  # Replace 1 with the ID of the document you want to summarize

# Handle case when document is not found
if document_content is None:
    print("Document not found")
    exit()

# Calculate remaining tokens for the model
MAX_TOKENS = 4097  # Davinci model's maximum token limit
remaining_tokens = 3000  # Reserve some tokens for the summary and other text

# Trim the document content to fit within the token limit
if len(document_content.split()) > remaining_tokens:
    trimmed_content = " ".join(document_content.split()[:remaining_tokens])
else:
    trimmed_content = document_content

# Use GPT-3 to summarize the document
if trimmed_content:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following document:\n{trimmed_content}",
        max_tokens=50  # Limiting to 50 tokens for the summary
    )
    summary = response.choices[0].text.strip()
    print(f"Summary: {summary}")
else:
    print("Document not found")
