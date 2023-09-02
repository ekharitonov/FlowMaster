# Step 1: Install Flask
# pip install Flask

# Step 2: Create a New Python File for the API
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Step 3: Create API Endpoints
## Get All Documents
@app.route('/documents', methods=['GET'])
def get_documents():
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Documents')
    documents = cursor.fetchall()
    conn.close()
    
    return jsonify({'documents': documents})

## Get a Single Document
@app.route('/documents/<int:doc_id>', methods=['GET'])
def get_document(doc_id):
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Documents WHERE id=?', (doc_id,))
    document = cursor.fetchone()
    conn.close()

    if document:
        return jsonify({'document': document})
    else:
        return jsonify({'error': 'Document not found'}), 404

## Add a New Document
@app.route('/documents', methods=['POST'])
def add_document():
    new_doc = request.json
    title = new_doc['title']
    content = new_doc['content']
    
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Documents (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Document added successfully'}), 201

# Step 4: Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
    
# Run python api.py
# Your API should now be running at http://127.0.0.1:5000/. You can test the API using tools like Postman or curl. 
# for example, to get all documents, you can use: curl http://127.0.0.1:5000/documents
# or, to add a new document: curl -X POST -H "Content-Type: application/json" -d '{"title": "New Document", "content": "This is a new document"}' http://127.0.0.1:5000/documents
