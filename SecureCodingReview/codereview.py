from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

# Function to initialize database
def init_db():
    with app.app_context():
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        db.commit()
        db.close()

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required'}), 400
    
    username = data['username']
    password = data['password']
    
    # Vulnerability: SQL Injection in the query
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    db.commit()
    db.close()
    
    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
