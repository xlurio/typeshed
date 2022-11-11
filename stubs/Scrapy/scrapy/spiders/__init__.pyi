from collections.abc import Generator
from logging import LoggerAdapter, Logger
from typing import Optional

from scrapy import signals as signals
from scrapy.crawler import Crawler
from scrapy.http import Request as Request
from scrapy.http.response.html import HtmlResponse
from scrapy.http.response.text import TextResponse
from scrapy.spiders.crawl import CrawlSpider as CrawlSpider, Rule as Rule
from scrapy.spiders.feed import CSVFeedSpider as CSVFeedSpider, XMLFeedSpider as XMLFeedSpider
from scrapy.spiders.sitemap import SitemapSpider as SitemapSpider
from scrapy.utils.trackref import object_ref as object_ref
from scrapy.utils.url import url_is_from_spider as url_is_from_spider

class Spider(object_ref):
    name: Optional[str]
    custom_settings: Optional[dict[str, str]]
    start_urls: list[str]
    def __init__(self, name: str | None = ..., **kwargs) -> None: ...
    @property
    def logger(self) -> LoggerAdapter[Logger]: ...
    def log(self, message: object, level: int = ..., **kw) -> None: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler, *args, **kwargs) -> Spider: ...
    def start_requests(self) -> Generator[Request, None, None]: ...
    def parse(self, response: HtmlResponse | TextResponse, **kwargs) -> None: ...
    @classmethod
    def update_settings(cls, settings) -> None: ...
    @classmethod
    def handles_request(cls, request): ...
    @staticmethod
    def close(spider, reason): ...
