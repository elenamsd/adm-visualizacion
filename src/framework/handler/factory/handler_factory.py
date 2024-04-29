from src.framework.handler.strategy.handler_context import HandlerContext
from src.framework.handler.strategy.impl.stop_and_search_handler import StopAndSearchHandler


class HandlerFactory:

    @staticmethod
    def create_handler(data_source_type: str) -> HandlerContext:
        if data_source_type == 'stop_and_search':
            return HandlerContext(StopAndSearchHandler())
        else:
            raise ValueError('Invalid data source type')
