from abc import abstractmethod
from typing import List
import pandas as pd
from src.framework.strategies.reader.reader_strategy import ReaderStrategy


class CsvReader(ReaderStrategy):

    @abstractmethod
    def get_files(self, path: str) -> List[str]:
        pass

    def get_dataframe(self, files: List[str]) -> pd.DataFrame:
        dfs: List[pd.DataFrame] = []
        for file in files:
            if file.endswith('.csv'):
                dfs.append(pd.read_csv(file))

        return pd.concat(dfs, ignore_index=True)
