from flask import Flask,request,render_template
from config import Config
from utils import OpenAi

# =========== CONFIG =========
app = Flask(__name__)
app.config.from_object(Config)

# =========== VIEWS ==========
@app.route("/", methods=['GET'])
def index():
    """
    Main Page View
    """

    return render_template('index.html')


@app.route("/api/chat/", methods=['POST'])
def chat():
    """
    API for get prompt ,send to api open-ai ,receive the answer and return it   

    Params :
        text : user's prompt
    
    Response :
        status : if ok it's work true and if bad it's have problem in connection to open-ai
        response : answer prompt(if status not's ok return None)
    """

    text = request.json.get('text')
    openai = OpenAi(app.config['API_KEY_OPENAI'])

    try:
        response = openai.chat_io(text)
        return {'status': 'ok', 'response': response}, 200
    except:
        return {'status': 'bad', 'response': None}, 500

# =========== RUN ============
if __name__ == '__main__':
    app.run()