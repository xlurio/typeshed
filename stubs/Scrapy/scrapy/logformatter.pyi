from _typeshed import Incomplete

from scrapy.utils.request import referer_str as referer_str

SCRAPEDMSG: Incomplete
DROPPEDMSG: Incomplete
CRAWLEDMSG: str
ITEMERRORMSG: str
SPIDERERRORMSG: str
DOWNLOADERRORMSG_SHORT: str
DOWNLOADERRORMSG_LONG: str

class LogFormatter:
    def crawled(self, request, response, spider): ...
    def scraped(self, item, response, spider): ...
    def dropped(self, item, exception, response, spider): ...
    def item_error(self, item, exception, response, spider): ...
    def spider_error(self, failure, request, response, spider): ...
    def download_error(self, failure, request, spider, errmsg: Incomplete | None = ...): ...
    @classmethod
    def from_crawler(cls, crawler): ...
