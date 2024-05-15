from typing import List

import pandas as pd

from src.framework.enum.datasource_type import DatasourceType
from src.framework.handler.handler_context import HandlerContext
from src.framework.handler.impl.stop_and_search_handler import StopAndSearchHandler
from src.framework.handler.impl.uk_accidents_handler import UKAccidentsHandler
from src.framework.reader.impl.csv_reader import CsvReader
from src.framework.reader.impl.stop_and_search_csv_reader import StopAndSearchCsvReader
from src.framework.reader.reader_context import ReaderContext


class DataframeFactory:

    @staticmethod
    def create_dataframe(datasource_type: DatasourceType) -> pd.DataFrame:
        if datasource_type.is_dyfed_powys() or datasource_type.is_cambridgeshire():
            return DataframeFactory._create_dataframe_stop_and_search(datasource_type.path)
        elif datasource_type.is_uk_accidents():
            return DataframeFactory._create_dataframe_uk_accidents(datasource_type.path)
        else:
            raise ValueError('Invalid data source type')

    @classmethod
    def _create_dataframe_stop_and_search(cls, path) -> pd.DataFrame:
        reader: ReaderContext = ReaderContext(StopAndSearchCsvReader())
        dataset: List[str] = reader.get_files(path)
        dataframe: pd.DataFrame = reader.get_dataframe(dataset)
        handler: HandlerContext = HandlerContext(StopAndSearchHandler())

        return handler.clean_dataframe(dataframe)

    @classmethod
    def _create_dataframe_uk_accidents(cls, path) -> pd.DataFrame:
        reader: ReaderContext = ReaderContext(CsvReader())
        dataset: List[str] = reader.get_files(path)
        dataframe: pd.DataFrame = reader.get_dataframe(dataset)
        handler: HandlerContext = HandlerContext(UKAccidentsHandler())

        return handler.clean_dataframe(dataframe)
