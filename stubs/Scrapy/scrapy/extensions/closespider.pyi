from _typeshed import Incomplete

from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured

class CloseSpider:
    crawler: Incomplete
    close_on: Incomplete
    counter: Incomplete
    def __init__(self, crawler) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def error_count(self, failure, response, spider) -> None: ...
    def page_count(self, response, request, spider) -> None: ...
    task: Incomplete
    def spider_opened(self, spider) -> None: ...
    def item_scraped(self, item, spider) -> None: ...
    def spider_closed(self, spider) -> None: ...
