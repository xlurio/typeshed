from _typeshed import Incomplete
from io import TextIOWrapper
from logging import Logger
from typing import Type, TypeVar

from scrapy.http.request import Request as Request
from scrapy.settings import BaseSettings as BaseSettings
from scrapy.spiders import Spider as Spider
from scrapy.utils.job import job_dir as job_dir
from scrapy.utils.request import referer_str as referer_str, request_fingerprint as request_fingerprint
from twisted.internet.defer import Deferred as Deferred

BaseDupeFilterTV = TypeVar("BaseDupeFilterTV", bound="BaseDupeFilter")

class BaseDupeFilter:
    @classmethod
    def from_settings(cls: Type[BaseDupeFilterTV], settings: BaseSettings) -> BaseDupeFilterTV: ...
    def request_seen(self, request: Request) -> bool: ...
    def open(self) -> Deferred[Incomplete] | None: ...
    def close(self, reason: str) -> Deferred[Incomplete] | None: ...
    def log(self, request: Request, spider: Spider) -> None: ...

RFPDupeFilterTV = TypeVar("RFPDupeFilterTV", bound="RFPDupeFilter")

class RFPDupeFilter(BaseDupeFilter):
    file: TextIOWrapper | None
    fingerprints: set[str]
    logdupes: bool
    debug: bool
    logger: Logger
    def __init__(self, path: str | None = ..., debug: bool = ...) -> None: ...
    @classmethod
    def from_settings(cls: Type[RFPDupeFilterTV], settings: BaseSettings) -> RFPDupeFilterTV: ...
    def request_seen(self, request: Request) -> bool: ...
    def request_fingerprint(self, request: Request) -> str: ...
    def close(self, reason: str) -> None: ...
    def log(self, request: Request, spider: Spider) -> None: ...
