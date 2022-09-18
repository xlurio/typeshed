from typing import Any, Callable, Union

from scrapy import Request as Request, Spider as Spider
from scrapy.http import Response as Response
from scrapy.middleware import MiddlewareManager as MiddlewareManager
from scrapy.utils.conf import build_component_list as build_component_list
from scrapy.utils.defer import mustbe_deferred as mustbe_deferred
from scrapy.utils.python import MutableChain as MutableChain
from twisted.internet.defer import Deferred as Deferred
from twisted.python.failure import Failure

ScrapeFunc = Callable[[Union[Response, Failure], Request, Spider], Any]

class SpiderMiddlewareManager(MiddlewareManager):
    component_name: str
    def scrape_response(self, scrape_func: ScrapeFunc, response: Response, request: Request, spider: Spider) -> Deferred: ...
    def process_start_requests(self, start_requests, spider: Spider) -> Deferred: ...
