from _typeshed import Incomplete
from collections.abc import Generator
from typing import Optional

from scrapy import signals as signals
from scrapy.http import Request as Request
from scrapy.spiders.crawl import CrawlSpider as CrawlSpider, Rule as Rule
from scrapy.spiders.feed import CSVFeedSpider as CSVFeedSpider, XMLFeedSpider as XMLFeedSpider
from scrapy.spiders.sitemap import SitemapSpider as SitemapSpider
from scrapy.utils.trackref import object_ref as object_ref
from scrapy.utils.url import url_is_from_spider as url_is_from_spider

class Spider(object_ref):
    name: Optional[str]
    custom_settings: Optional[dict]
    start_urls: Incomplete
    def __init__(self, name: Incomplete | None = ..., **kwargs) -> None: ...
    @property
    def logger(self): ...
    def log(self, message, level=..., **kw) -> None: ...
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs): ...
    def start_requests(self) -> Generator[Incomplete, None, None]: ...
    def parse(self, response, **kwargs) -> None: ...
    @classmethod
    def update_settings(cls, settings) -> None: ...
    @classmethod
    def handles_request(cls, request): ...
    @staticmethod
    def close(spider, reason): ...
