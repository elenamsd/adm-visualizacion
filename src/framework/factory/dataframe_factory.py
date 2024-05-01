from typing import List

import pandas as pd

from src.framework.enum.datasource_type import DatasourceType
from src.framework.strategy.handler.handler_context import HandlerContext
from src.framework.strategy.handler.impl.stop_and_search_handler import StopAndSearchHandler
from src.framework.strategy.reader.impl.stop_and_search_csv_reader import StopAndSearchCsvReader
from src.framework.strategy.reader.reader_context import ReaderContext


class DataframeFactory:

    @staticmethod
    def create_dataframe(datasource_type: DatasourceType) -> pd.DataFrame:
        if datasource_type.is_dyfed_powys():
            return DataframeFactory._create_dataframe_stop_and_search(DatasourceType.STOP_AND_SEARCH_DYFED_POWYS.path)
        else:
            raise ValueError('Invalid data source type')

    @classmethod
    def _create_dataframe_stop_and_search(cls, path) -> pd.DataFrame:
        reader: ReaderContext = ReaderContext(StopAndSearchCsvReader())
        dataset: List[str] = reader.get_files(path)
        dataframe: pd.DataFrame = reader.get_dataframe(dataset)
        handler: HandlerContext = HandlerContext(StopAndSearchHandler())

        return handler.clean_dataframe(dataframe)
