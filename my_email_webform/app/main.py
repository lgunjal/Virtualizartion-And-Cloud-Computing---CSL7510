from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Initialize the SQLite database
def init_sqlite_db():
    if not os.path.exists('app/database.db'):
        conn = sqlite3.connect('app/database.db')
        print("Opened database successfully")
        conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
        print("Table created successfully")
        conn.close()

init_sqlite_db()

@app.route('/')
def home():
    conn = sqlite3.connect('app/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if name and email:
            conn = sqlite3.connect('app/database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            conn.close()
            return redirect('/')
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
