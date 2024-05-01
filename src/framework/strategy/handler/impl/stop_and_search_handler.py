import pandas as pd

from src.framework.strategy.handler.handler_strategy import HandlerStrategy


class StopAndSearchHandler(HandlerStrategy):

    def clean_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.drop(columns=['Part of a policing operation', 'Policing operation', 'Legislation', 'Outcome linked to object of search', 'Removal of more than just outer clothing'])
        dataframe = dataframe.drop(columns=['Latitude', 'Longitude'])
        dataframe = dataframe.dropna(axis=0, how='any')

        dataframe['Date'] = pd.to_datetime(dataframe['Date'])

        print(dataframe.info())
        return dataframe
