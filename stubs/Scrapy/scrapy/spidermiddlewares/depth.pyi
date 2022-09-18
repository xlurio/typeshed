from _typeshed import Incomplete

from scrapy.http import Request as Request

logger: Incomplete

class DepthMiddleware:
    maxdepth: Incomplete
    stats: Incomplete
    verbose_stats: Incomplete
    prio: Incomplete
    def __init__(self, maxdepth, stats, verbose_stats: bool = ..., prio: int = ...) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_spider_output(self, response, result, spider): ...
