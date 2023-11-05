from contextlib import nullcontext as does_not_raise

from chess_analysis.scraper.utils import PGNParser


def test_parses_pgn():
    pgn_string = '''[Event "Live Chess"]
[Site "Chess.com"]
[Date "2020.12.20"]
[Round "-"]
[White "elucidator03"]
[Black "haseebyousaf"]
[Result "0-1"]
[CurrentPosition "rnbqkb1r/ppp2ppp/4pn2/8/2BP4/4P3/PP3PPP/RNBQK1NR w KQkq -"]
[Timezone "UTC"]
[ECO "D20"]
[ECOUrl "https://www.chess.com/openings/Queens-Gambit-Accepted-Old-Variation-3...Nf6-4.Bxc4-e6"]
[UTCDate "2020.12.20"]
[UTCTime "14:16:52"]
[WhiteElo "1021"]
[BlackElo "1201"]
[TimeControl "600"]
[Termination "haseebyousaf won - game abandoned"]
[StartTime "14:16:52"]
[EndDate "2020.12.20"]
[EndTime "14:18:44"]
[Link "https://www.chess.com/game/live/6013832307"]

1. d4 {[%clk 0:09:56.6]} 1... d5 {[%clk 0:09:58]} 2. c4 {[%clk 0:09:54.9]} 2... dxc4 {[%clk 0:09:53.4]} 3. e3 {[%clk 0:09:53.1]} 3... Nf6 {[%clk 0:09:38.7]} 4. Bxc4 {[%clk 0:09:50.2]} 4... e6 {[%clk 0:09:22.2]} 0-1"
'''
    pgn_parser = PGNParser()
    with does_not_raise():
        result = pgn_parser.parse(pgn_string)
    assert result

