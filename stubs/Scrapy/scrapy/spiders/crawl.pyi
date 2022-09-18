from _typeshed import Incomplete
from typing import Sequence

from scrapy.http import HtmlResponse as HtmlResponse, Request as Request
from scrapy.linkextractors import LinkExtractor as LinkExtractor
from scrapy.spiders import Spider as Spider
from scrapy.utils.spider import iterate_spider_output as iterate_spider_output

class Rule:
    link_extractor: Incomplete
    callback: Incomplete
    errback: Incomplete
    cb_kwargs: Incomplete
    process_links: Incomplete
    process_request: Incomplete
    follow: Incomplete
    def __init__(
        self,
        link_extractor: Incomplete | None = ...,
        callback: Incomplete | None = ...,
        cb_kwargs: Incomplete | None = ...,
        follow: Incomplete | None = ...,
        process_links: Incomplete | None = ...,
        process_request: Incomplete | None = ...,
        errback: Incomplete | None = ...,
    ) -> None: ...

class CrawlSpider(Spider):
    rules: Sequence[Rule]
    def __init__(self, *a, **kw) -> None: ...
    def parse_start_url(self, response, **kwargs): ...
    def process_results(self, response, results): ...
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs): ...
