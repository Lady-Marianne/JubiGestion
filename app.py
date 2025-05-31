from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the home page:
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# This is a simple Flask application that serves a home page.
# To run this application, save it as app.py and execute it with Python.
