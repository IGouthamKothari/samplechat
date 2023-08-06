from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('OPENAI_API_KEY')

app = Flask(__name__)

openai.api_key = API_KEY


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = openai.Completion.create(engine="text-davinci-003", prompt=user_input, max_tokens=2000)
    return jsonify(response.choices[0].text.strip())


if __name__ == '__main__':
    app.run(debug=True)
