import typer

from . import config
from .scraper import (
    ChessComScraper,
    LichessScraper,
    UserNotFoundException
)


app = typer.Typer()


@app.command()
def scrape_chess_com(username: str):
    scraper = ChessComScraper(config.CHESS_COM_BASE_URL)
    try:
        scraper.scrape_user(username)
    except UserNotFoundException:
        print(f'\nCan not find user with username {username}!\n')
    else:
        print('\nSuccessfully saved user info in data folder\n')


@app.command()
def scrape_lichess(username: str):
    pass


if __name__ == '__main__':
    app()

