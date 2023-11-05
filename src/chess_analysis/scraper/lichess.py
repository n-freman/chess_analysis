from typing import Self

from .abstract import AbstractScraper
from .mixins import CSVSaverMixin


class LichessScraper(CSVSaverMixin, AbstractScraper):

    def __init__(self, base_url: str):
        self.base_url = base_url

    def scrape_user(self: Self, username: str):
        pass

