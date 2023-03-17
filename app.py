from flask import Flask
from flask import render_template
from config import Config
from flask import request

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/", methods=['GET'])
def index():
    context = {
        "name":'pooya',
    }

    return render_template('index.html',**context)

@app.route("/api/chat/", methods=['POST'])
def chat():
    text = request.json.get('text')

    return {'status': 'ok', 'response': text}

if __name__ == '__main__':
    app.run()