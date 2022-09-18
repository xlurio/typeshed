from _typeshed import Incomplete
from abc import abstractmethod
from typing import Optional, TypeVar

from scrapy.crawler import Crawler as Crawler
from scrapy.http.request import Request as Request
from scrapy.spiders import Spider as Spider
from scrapy.utils.job import job_dir as job_dir
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from twisted.internet.defer import Deferred as Deferred

logger: Incomplete

class BaseSchedulerMeta(type):
    def __instancecheck__(cls, instance): ...
    def __subclasscheck__(cls, subclass): ...

class BaseScheduler(metaclass=BaseSchedulerMeta):
    @classmethod
    def from_crawler(cls, crawler: Crawler): ...
    def open(self, spider: Spider) -> Optional[Deferred]: ...
    def close(self, reason: str) -> Optional[Deferred]: ...
    @abstractmethod
    def has_pending_requests(self) -> bool: ...
    @abstractmethod
    def enqueue_request(self, request: Request) -> bool: ...
    @abstractmethod
    def next_request(self) -> Optional[Request]: ...

SchedulerTV = TypeVar("SchedulerTV", bound="Scheduler")

class Scheduler(BaseScheduler):
    df: Incomplete
    dqdir: Incomplete
    pqclass: Incomplete
    dqclass: Incomplete
    mqclass: Incomplete
    logunser: Incomplete
    stats: Incomplete
    crawler: Incomplete
    def __init__(
        self,
        dupefilter,
        jobdir: Optional[str] = ...,
        dqclass: Incomplete | None = ...,
        mqclass: Incomplete | None = ...,
        logunser: bool = ...,
        stats: Incomplete | None = ...,
        pqclass: Incomplete | None = ...,
        crawler: Optional[Crawler] = ...,
    ) -> None: ...
    @classmethod
    def from_crawler(cls, crawler) -> SchedulerTV: ...
    def has_pending_requests(self) -> bool: ...
    spider: Incomplete
    mqs: Incomplete
    dqs: Incomplete
    def open(self, spider: Spider) -> Optional[Deferred]: ...
    def close(self, reason: str) -> Optional[Deferred]: ...
    def enqueue_request(self, request: Request) -> bool: ...
    def next_request(self) -> Optional[Request]: ...
    def __len__(self) -> int: ...
