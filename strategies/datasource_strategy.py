from abc import ABC, abstractmethod


class DatasourceStrategy(ABC):

    @abstractmethod
    def get_dataframe(self, files) -> None:
        pass
