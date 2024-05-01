from typing import List

import pandas as pd

from src.framework.strategy.reader.reader_strategy import ReaderStrategy


class ReaderContext:

    def __init__(self, strategy: ReaderStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> ReaderStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ReaderStrategy) -> None:
        self._strategy = strategy

    def get_dataframe(self, files: List[str]) -> pd.DataFrame:
        return self._strategy.get_dataframe(files)

    def get_files(self, path: str) -> List[str]:
        return self._strategy.get_files(path)
