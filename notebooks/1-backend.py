# 1. Backend Development with Flask:
## Setting up a basic Flask app:

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, FlowMaster!")

if __name__ == '__main__':
    app.run(debug=True)
