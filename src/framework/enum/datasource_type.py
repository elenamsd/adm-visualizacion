from enum import Enum
from typing import List

DATA_FOLDER = '../../data'


class DatasourceType(Enum):

    STOP_AND_SEARCH_DYFED_POWYS = ("Dyfed Powys - Stop and Search", f"{DATA_FOLDER}/stop-and-search/dyfed-powys/")
    STOP_AND_SEARCH_CAMBRIDGESHIRE = ("Cambridgeshire - Stop and Search", f"{DATA_FOLDER}/stop-and-search/cambridgeshire/")
    UK_ACCIDENTS = ("United Kingdom - Accidents ", f"{DATA_FOLDER}/uk-accidents/")

    def __new__(cls, name: str, path: str) -> Enum:
        datasource_type = object.__new__(cls)
        datasource_type._name = name
        datasource_type._path = path
        return datasource_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        return self._path

    @classmethod
    def list(cls) -> List['DatasourceType']:
        return [datasource_type for datasource_type in cls]

    def is_dyfed_powys(self) -> bool:
        return self == DatasourceType.STOP_AND_SEARCH_DYFED_POWYS

    def is_cambridgeshire(self) -> bool:
        return self == DatasourceType.STOP_AND_SEARCH_CAMBRIDGESHIRE

    def is_uk_accidents(self) -> bool:
        return self == DatasourceType.UK_ACCIDENTS
