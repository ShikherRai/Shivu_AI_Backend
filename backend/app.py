from flask import Flask, request, jsonify
from flask_cors import CORS
import pyttsx3

app = Flask(__name__)
CORS(app)

tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)

def speak_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm an AI, but I'm here to help!",
        "bye": "Goodbye! Have a great day!",
        "who are you": "I am Shivu, your AI assistant!"
    }
    
    bot_response = responses.get(user_message.lower(), "I'm not sure how to respond to that.")
    
    speak_text(bot_response)
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
