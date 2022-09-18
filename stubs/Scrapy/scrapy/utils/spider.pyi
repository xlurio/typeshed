from _typeshed import Incomplete
from collections.abc import Generator

from scrapy.spiders import Spider as Spider
from scrapy.utils.asyncgen import collect_asyncgen as collect_asyncgen
from scrapy.utils.defer import deferred_from_coro as deferred_from_coro
from scrapy.utils.misc import arg_to_iter as arg_to_iter

logger: Incomplete

def iterate_spider_output(result): ...
def iter_spider_classes(module) -> Generator[Incomplete, None, None]: ...
def spidercls_for_request(
    spider_loader, request, default_spidercls: Incomplete | None = ..., log_none: bool = ..., log_multiple: bool = ...
): ...

class DefaultSpider(Spider):
    name: str
