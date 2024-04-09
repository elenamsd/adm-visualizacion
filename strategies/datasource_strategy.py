from abc import ABC, abstractmethod
import pandas as pd


class DatasourceStrategy(ABC):

    @abstractmethod
    def get_dataframe(self, files) -> pd.DataFrame:
        pass
