from abc import ABC, abstractmethod
from typing import List

import pandas as pd


class ReaderStrategy(ABC):

    @abstractmethod
    def get_dataframe(self, files: List[str]) -> pd.DataFrame:
        pass

    def get_files(self, path: str) -> List[str]:
        pass
