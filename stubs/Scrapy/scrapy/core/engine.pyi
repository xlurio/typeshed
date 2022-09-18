from _typeshed import Incomplete
from typing import Callable, Iterable, Optional

from scrapy import signals as signals
from scrapy.core.scraper import Scraper as Scraper
from scrapy.exceptions import (
    CloseSpider as CloseSpider,
    DontCloseSpider as DontCloseSpider,
    ScrapyDeprecationWarning as ScrapyDeprecationWarning,
)
from scrapy.http import Request as Request, Response as Response
from scrapy.settings import BaseSettings as BaseSettings
from scrapy.spiders import Spider as Spider
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info, logformatter_adapter as logformatter_adapter
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.reactor import CallLaterOnce as CallLaterOnce
from twisted.internet.defer import Deferred

logger: Incomplete

class Slot:
    closing: Incomplete
    inprogress: Incomplete
    start_requests: Incomplete
    close_if_idle: Incomplete
    nextcall: Incomplete
    scheduler: Incomplete
    heartbeat: Incomplete
    def __init__(self, start_requests: Iterable, close_if_idle: bool, nextcall: CallLaterOnce, scheduler) -> None: ...
    def add_request(self, request: Request) -> None: ...
    def remove_request(self, request: Request) -> None: ...
    def close(self) -> Deferred: ...

class ExecutionEngine:
    crawler: Incomplete
    settings: Incomplete
    signals: Incomplete
    logformatter: Incomplete
    slot: Incomplete
    spider: Incomplete
    running: bool
    paused: bool
    scheduler_cls: Incomplete
    downloader: Incomplete
    scraper: Incomplete
    def __init__(self, crawler, spider_closed_callback: Callable) -> None: ...
    start_time: Incomplete
    def start(self) -> Deferred: ...
    def stop(self) -> Deferred: ...
    def close(self) -> Deferred: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def spider_is_idle(self, spider: Optional[Spider] = ...) -> bool: ...
    def crawl(self, request: Request, spider: Optional[Spider] = ...) -> None: ...
    def download(self, request: Request, spider: Optional[Spider] = ...) -> Deferred: ...
    def open_spider(self, spider: Spider, start_requests: Iterable = ..., close_if_idle: bool = ...): ...
    def close_spider(self, spider: Spider, reason: str = ...) -> Deferred: ...
    @property
    def open_spiders(self) -> list: ...
    def has_capacity(self) -> bool: ...
    def schedule(self, request: Request, spider: Spider) -> None: ...
