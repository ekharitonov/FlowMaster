# Code for Developing an Easy MVP for Process Mapping and Basic Analytics in User Interface

## Backend Code (Python + Flask)

# Importing required libraries
from flask import Flask, render_template, request
import json

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get process data from the form
        process_data = request.form.get('process_data')
        # Convert the process data to a Python dictionary
        process_dict = json.loads(process_data)
        # Perform basic analytics (e.g., count the number of steps in the process)
        num_steps = len(process_dict.get('steps', []))
        return render_template('index.html', num_steps=num_steps)
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
