from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from chatbot import getResponse

app = Flask(__name__)

# SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the Conversation model
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(200), nullable=False)
    bot_response = db.Column(db.String(200), nullable=False)

# Initialize the database (First-time run to create tables)
with app.app_context():
    db.create_all()

# The function to return "Hi"
def chatbot_reply(input_text):
    return "Hi"

# Home route (Main page)
@app.route('/')
def index():
    # Get all previous conversations from the database
    conversations = Conversation.query.all()
    return render_template('index.html', conversations=conversations)

# Route to handle new user input
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('user_input')

    # Get the bot response (for now, always "Hi")
    bot_response = chatbot_reply(user_input)

    # Save the conversation to the database
    new_conversation = Conversation(user_input=user_input, bot_response=bot_response)
    db.session.add(new_conversation)
    db.session.commit()

    return jsonify({
        'user_input': user_input,
        'bot_response': bot_response
    })

if __name__ == '__main__':
    app.run(debug=True)
