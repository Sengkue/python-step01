from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # You can process the form data here (e.g., store in a database)
    # For now, we will just return the user's input as a message
    return f"Thanks for contacting us, {name}! We received your message: {message}"

if __name__ == '__main__':
    app.run(debug=True)
