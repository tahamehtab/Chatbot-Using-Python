import google.generativeai as genai
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

os.environ["API_KEY"] = os.getenv("API_KEY")
# I saved my API key in enviroment variables and call it directly here 
# so that it cannot be spoiled so for testing use your own Gemini API key.

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']
    bot_response = model.generate_content([user_message])

    # Format the response for better readability
    formatted_response = bot_response.text.replace('\n', '<br>').replace('  ', '&nbsp;&nbsp;').replace('*', '')

    return jsonify({'response': formatted_response})

if __name__ == '__main__':
    app.run(debug=True)