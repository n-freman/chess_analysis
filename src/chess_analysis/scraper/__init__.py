import httpx
from tenacity import retry

from .abstract import AbstractScraper
from .exceptions import UserNotFoundException
from .chess_com import ChessComScraper
from .lichess import LichessScraper

httpx.get = retry(httpx.get)

__all__ = [
    'AbstractScraper',
    'ChessComScraper',
    'LichessScraper',
    'UserNotFoundException',
]

