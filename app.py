from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy chatbot logic – replace with your real logic if needed
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # Example response logic
    if user_message.lower() == 'hello':
        bot_reply = "Hi there! How can I help you?"
    else:
        bot_reply = f"You said: {user_message}"

    return jsonify({'response': bot_reply})

# Health check route
@app.route('/', methods=['GET'])
def home():
    return "Chatbot API is live!"
