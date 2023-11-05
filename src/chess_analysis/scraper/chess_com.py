from typing import Self

import httpx
from tqdm import tqdm

from .abstract import AbstractScraper
from .exceptions import UserNotFoundException
from .mixins import CSVSaverMixin
from .utils import PGNParser

class ChessComScraper(CSVSaverMixin, AbstractScraper):

    def __init__(self, base_url: str):
        self.base_url = base_url

    def scrape_user(self: Self, username: str):
        pgn_parser = PGNParser()
        response = httpx.get(f'{self.base_url}/{username}/games/archives')
        if response.status_code == 404:
            raise UserNotFoundException
        games = []
        for archive in tqdm(response.json()['archives']):
            response = httpx.get(archive)
            games.extend(response.json()['games'])
        for game in games:
            if game.get('pgn') is None:
                continue
            game.update(pgn_parser.parse(game['pgn']))
            del game['pgn']
        self._save(
            f'data/chess_com_{username}_games.csv',
            games
        )        
 
