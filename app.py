from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
DATA_FILE = 'passwords.json'

# Load existing data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save data
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = load_data()
    website = request.form['website']
    username = request.form['username']
    password = request.form['password']

    data[website] = {
        'username': username,
        'password': password
    }

    save_data(data)
    return 'Password saved successfully!'

@app.route('/get', methods=['GET'])
def get():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
