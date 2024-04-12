import pandas as pd
from src.framework.strategies.handler.handler_strategy import HandlerStrategy


class HandlerContext:

    def __init__(self, strategy: HandlerStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> HandlerStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: HandlerStrategy) -> None:
        self._strategy = strategy

    def clean_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        return self._strategy.clean_dataframe(dataframe)
