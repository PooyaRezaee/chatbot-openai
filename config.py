import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')