from typing import List
import pandas as pd
from strategies.datasource_strategy import DatasourceStrategy


class CSVStrategy(DatasourceStrategy):

    def get_dataframe(self, files: List[str]) -> pd.DataFrame:
        dfs: List[pd.DataFrame] = []
        for file in files:
            if file.endswith('.csv'):
                dfs.append(pd.read_csv(file))

        return pd.concat(dfs, ignore_index=True)
