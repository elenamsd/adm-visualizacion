import os
from typing import List

import pandas as pd

from src.framework.strategy.reader.reader_strategy import ReaderStrategy


class CsvReader(ReaderStrategy):

    def get_files(self, path: str) -> List[str]:
        dataset: List[str] = []
        for file in os.listdir(path):
            if file.endswith('.csv') and not file.startswith('output'):
                dataset.append(os.path.join(path, file))

        return dataset

    def get_dataframe(self, files: List[str]) -> pd.DataFrame:
        dfs: List[pd.DataFrame] = []
        for file in files:
            if file.endswith('.csv'):
                dfs.append(pd.read_csv(file))

        return pd.concat(dfs, ignore_index=True)
