from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

if __name__ == '__main__':
    app.run()
