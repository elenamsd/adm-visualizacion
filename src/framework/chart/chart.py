from abc import ABC, abstractmethod
from typing import List

import pandas as pd


class Chart(ABC):

    def __init__(self, dataframe: pd.DataFrame, title: str, columns: List[str]) -> None:
        self._dataframe = dataframe
        self._title = title
        self._columns = columns

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._dataframe

    @property
    def title(self) -> str:
        return self._title

    @property
    def columns(self) -> List[str]:
        return self._columns

    @abstractmethod
    def plot(self) -> None:
        pass
