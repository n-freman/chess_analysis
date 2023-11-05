from typing import Mapping, Self
from abc import ABC, abstractmethod


class AbstractScraper(ABC):

    @abstractmethod
    def __init__(self: Self, base_url: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def scrape_user(self: Self, username: str):
        raise NotImplementedError

    @abstractmethod
    def _save(
        self: Self,
        filepath: str,
        data: Mapping
    ) -> None:
        raise NotImplementedError

