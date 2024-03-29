import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    """
    Variables for config project
    """
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    API_KEY_OPENAI = os.environ.get('API_KEY_OPENAI')