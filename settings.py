import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("api_key")
API_KEY_SECRET = os.environ.get("api_key_secret")
ACCESS_TOKEN = os.environ.get("access_token")
ACCESS_TOKEN_SECRET = os.environ.get("access_token_secret")