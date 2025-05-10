from flask import Flask, request, jsonify
from chatbot import get_bot_response
from config import API_KEY

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_key = request.headers.get('x-api-key')
    message = data.get("message", "")

    if user_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    if not message:
        return jsonify({"error": "Empty message"}), 400

    response = get_bot_response(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
