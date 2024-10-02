import mysql.connector

DATABASE_CONFIG = {
    'user': 'root',       # default user for XAMPP
    'password': '',       # leave empty if there's no password
    'host': '127.0.0.1',  # localhost
    'database': 'powerbi' # your database name
}

def get_db_connection():
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    return conn

def create_post(title, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, content) VALUES (%s, %s)', (title, content))
    conn.commit()
    cursor.close()
    conn.close()

def get_posts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts

def get_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM posts WHERE id = %s', (post_id,))
    post = cursor.fetchone()
    cursor.close()
    conn.close()
    return post

def update_post(post_id, title, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE posts SET title = %s, content = %s WHERE id = %s', (title, content, post_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM posts WHERE id = %s', (post_id,))
    conn.commit()
    cursor.close()
    conn.close()
