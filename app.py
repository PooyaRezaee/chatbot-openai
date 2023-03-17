from flask import Flask
from flask import render_template
from config import Config
from flask import request

from utils import OpenAi

# =========== CONFIG =========
app = Flask(__name__)
app.config.from_object(Config)

# =========== VIEWS =========
@app.route("/", methods=['GET']) # Show Index Template 
def index():
    context = {
        "name":'pooya',
    }

    return render_template('index.html',**context)

@app.route("/api/chat/", methods=['POST']) # API ==> get text -> send for open ai -> return response in json for Index template
def chat():
    text = request.json.get('text')
    openai = OpenAi(app.config['API_KEY_OPENAI'])
    response = openai.chat_io(text)

    return {'status': 'ok', 'response': response}

# ============= RUN ===========
if __name__ == '__main__':
    app.run()