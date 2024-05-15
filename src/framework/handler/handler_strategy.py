from abc import ABC, abstractmethod

import pandas as pd


class HandlerStrategy(ABC):

    @abstractmethod
    def clean_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        pass
