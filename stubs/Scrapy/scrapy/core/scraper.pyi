from _typeshed import Incomplete
from typing import Iterable, Tuple, Union

from scrapy import Spider as Spider, signals as signals
from scrapy.core.spidermw import SpiderMiddlewareManager as SpiderMiddlewareManager
from scrapy.exceptions import CloseSpider as CloseSpider, DropItem as DropItem, IgnoreRequest as IgnoreRequest
from scrapy.http import Request as Request, Response as Response
from scrapy.utils.defer import (
    defer_fail as defer_fail,
    defer_succeed as defer_succeed,
    iter_errback as iter_errback,
    parallel as parallel,
)
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info, logformatter_adapter as logformatter_adapter
from scrapy.utils.misc import (
    load_object as load_object,
    warn_on_generator_with_return_value as warn_on_generator_with_return_value,
)
from scrapy.utils.spider import iterate_spider_output as iterate_spider_output
from twisted.internet.defer import Deferred
from twisted.python.failure import Failure

QueueTuple = Tuple[Union[Response, Failure], Request, Deferred]
logger: Incomplete

class Slot:
    MIN_RESPONSE_SIZE: int
    max_active_size: Incomplete
    queue: Incomplete
    active: Incomplete
    active_size: int
    itemproc_size: int
    closing: Incomplete
    def __init__(self, max_active_size: int = ...) -> None: ...
    def add_response_request(self, result: Union[Response, Failure], request: Request) -> Deferred: ...
    def next_response_request_deferred(self) -> QueueTuple: ...
    def finish_response(self, result: Union[Response, Failure], request: Request) -> None: ...
    def is_idle(self) -> bool: ...
    def needs_backout(self) -> bool: ...

class Scraper:
    slot: Incomplete
    spidermw: Incomplete
    itemproc: Incomplete
    concurrent_items: Incomplete
    crawler: Incomplete
    signals: Incomplete
    logformatter: Incomplete
    def __init__(self, crawler) -> None: ...
    def open_spider(self, spider: Spider): ...
    def close_spider(self, spider: Spider) -> Deferred: ...
    def is_idle(self) -> bool: ...
    def enqueue_scrape(self, result: Union[Response, Failure], request: Request, spider: Spider) -> Deferred: ...
    def call_spider(self, result: Union[Response, Failure], request: Request, spider: Spider) -> Deferred: ...
    def handle_spider_error(self, _failure: Failure, request: Request, response: Response, spider: Spider) -> None: ...
    def handle_spider_output(self, result: Iterable, request: Request, response: Response, spider: Spider) -> Deferred: ...
