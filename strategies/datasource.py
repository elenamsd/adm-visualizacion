from typing import List
import pandas as pd
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

    def get_dataframe(self, files: List) -> pd.DataFrame:
        return self._strategy.get_dataframe(files)
