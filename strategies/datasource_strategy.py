from abc import ABC, abstractmethod
from typing import List
import pandas as pd


class DatasourceStrategy(ABC):

    @abstractmethod
    def get_dataframe(self, files: List[str]) -> pd.DataFrame:
        pass
