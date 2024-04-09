from typing import List
from strategies.datasource_strategy import DatasourceStrategy


class Datasource:

    def __init__(self, strategy: DatasourceStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> DatasourceStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: DatasourceStrategy) -> None:
        self._strategy = strategy

    def get_dataframe(self, files: List):
        return self._strategy.get_dataframe(files)
