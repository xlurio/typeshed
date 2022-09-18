from typing import Callable

from scrapy import Spider as Spider
from scrapy.http import Request as Request, Response as Response
from scrapy.middleware import MiddlewareManager as MiddlewareManager
from scrapy.utils.conf import build_component_list as build_component_list
from scrapy.utils.defer import deferred_from_coro as deferred_from_coro, mustbe_deferred as mustbe_deferred
from twisted.python.failure import Failure as Failure

class DownloaderMiddlewareManager(MiddlewareManager):
    component_name: str
    def download(self, download_func: Callable, request: Request, spider: Spider): ...
