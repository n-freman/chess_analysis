import os

from dotenv import load_dotenv

load_dotenv('.env')

CHESS_COM_BASE_URL = 'https://api.chess.com/pub/player'

LICHESS_BASE_URL = 'https://lichess.org'
LICHESS_API_TOKEN = os.getenv('LICHESS_API_TOKEN')

