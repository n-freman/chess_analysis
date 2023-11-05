from typing import Dict, List, Self


class PGNParser:
    '''
    Class for parsing pgn string into dictionary.
    PGN is a notaion for storing chess games meta data.
    '''

    def parse(self: Self, pgn_string: str) -> Dict[str, str]:
        lines: List[str] = pgn_string.strip().split('\n')
        result: Dict[str, str] = {}
        # Not iterating over the last two lines,
        # beacuse they got to be parsed manually
        # due to different format
        for line in lines[:-2]:
            line = self._remove_extra_signs(line)
            result.update(self._get_key_value(line))
        result['moves'] = lines[-1]
        return result

    @staticmethod
    def _remove_extra_signs(line: str):
        '''
        Args:
            line: Line of pgn string

        Returns:
            Cleaned up line without signs like []""
        '''
        return line.replace('[', '').replace(']', '').replace('"', '')

    @staticmethod
    def _get_key_value(line: str) -> Dict[str, str]:
        '''
        Args:
            line: Line of pgn string
        Returns:
            Dictionary with one key-value pair
                corresponding for the given pgn line
        '''
        first_space = line.index(' ')
        key, value = line[:first_space], line[first_space+1:]
        return {key: value}

