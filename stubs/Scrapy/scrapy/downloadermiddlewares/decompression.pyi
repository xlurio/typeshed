from _typeshed import Incomplete

from scrapy.responsetypes import responsetypes as responsetypes

logger: Incomplete

class DecompressionMiddleware:
    def __init__(self) -> None: ...
    def process_response(self, request, response, spider): ...
