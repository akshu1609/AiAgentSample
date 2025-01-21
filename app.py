from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def home():
    return "Welcome to the Flask Project!"

# Example route for a specific feature
@app.route('/feature')
def feature():
    return "This is a feature page!"

# Route to demonstrate form handling
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form['data']  # Replace 'data' with the actual form field name
        return f"You submitted: {data}"
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
