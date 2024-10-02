from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# Create the database table
database.create_table()

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

# Route for creating a new post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        database.create_post(title, content)
        return redirect(url_for('view_posts'))
    return render_template('create_post.html')

# Route to view all posts
@app.route('/posts')
def view_posts():
    posts = database.get_posts()
    return render_template('posts.html', posts=posts)

# Route to view a single post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = database.get_post(post_id)
    return render_template('post.html', post=post)

# Route for updating a post
@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    post = database.get_post(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        database.update_post(post_id, title, content)
        return redirect(url_for('view_posts'))
    return render_template('update_post.html', post=post)

# Route for deleting a post
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    database.delete_post(post_id)
    return redirect(url_for('view_posts'))

if __name__ == '__main__':
    app.run(debug=True)
