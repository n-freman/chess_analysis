from typing import Self, List, Mapping

from pandas import DataFrame


class CSVSaverMixin:

    def _save(
        self: Self,
        filepath: str,
        data: List[Mapping]
    ) -> None:
        DataFrame(data).to_csv(filepath)

