from flask import Flask, render_template, request, redirect
import mariadb
import sys

app = Flask(__name__)

# Connect to MariaDB
try:
    conn = mariadb.connect(
        user="root",
        password="",        # leave empty if you didn't set a password
        host="localhost",
        port=3306,
        database="try"
    )
    cursor = conn.cursor()
except mariadb.Error as e:
    print(f"Database connection error: {e}")
    sys.exit(1)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
    except mariadb.Error as e:
        return f"Error: {e}"
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
