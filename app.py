from flask import Flask
from flask import render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/", methods=['GET'])
def index():
    context = {
        "name":'pooya',
    }

    return render_template('index.html',**context)


if __name__ == '__main__':
    app.run()