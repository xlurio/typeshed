from _typeshed import Incomplete
from logging import Logger
from typing import Optional, Union

from scrapy.core.downloader.handlers.http11 import TunnelError as TunnelError
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.http.request import Request as Request
from scrapy.spiders import Spider as Spider
from scrapy.utils.python import global_object_name as global_object_name
from scrapy.utils.response import response_status_message as response_status_message

retry_logger: Incomplete

def get_retry_request(
    request: Request,
    *,
    spider: Spider,
    reason: Union[str, Exception] = ...,
    max_retry_times: Optional[int] = ...,
    priority_adjust: Optional[int] = ...,
    logger: Logger = ...,
    stats_base_key: str = ...,
): ...

class RetryMiddleware:
    EXCEPTIONS_TO_RETRY: Incomplete
    max_retry_times: Incomplete
    retry_http_codes: Incomplete
    priority_adjust: Incomplete
    def __init__(self, settings) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_response(self, request, response, spider): ...
    def process_exception(self, request, exception, spider): ...
