from _typeshed import Incomplete
from typing import Callable, List, Optional, Tuple, TypeVar, Union

import scrapy
from scrapy.http.common import obsolete_setter as obsolete_setter
from scrapy.http.headers import Headers as Headers
from scrapy.utils.curl import curl_to_request_kwargs as curl_to_request_kwargs
from scrapy.utils.python import to_bytes as to_bytes
from scrapy.utils.trackref import object_ref as object_ref
from scrapy.utils.url import escape_ajax as escape_ajax

RequestTypeVar = TypeVar("RequestTypeVar", bound="Request")

class Request(object_ref):
    attributes: Tuple[str, ...]
    method: Incomplete
    priority: Incomplete
    callback: Incomplete
    errback: Incomplete
    cookies: Incomplete
    headers: Incomplete
    dont_filter: Incomplete
    flags: Incomplete
    def __init__(
        self,
        url: str,
        callback: Optional[Callable] = ...,
        method: str = ...,
        headers: Optional[dict] = ...,
        body: Optional[Union[bytes, str]] = ...,
        cookies: Optional[Union[dict, List[dict]]] = ...,
        meta: Optional[dict] = ...,
        encoding: str = ...,
        priority: int = ...,
        dont_filter: bool = ...,
        errback: Optional[Callable] = ...,
        flags: Optional[List[str]] = ...,
        cb_kwargs: Optional[dict] = ...,
    ) -> None: ...
    @property
    def cb_kwargs(self) -> dict: ...
    @property
    def meta(self) -> dict: ...
    url: Incomplete
    body: Incomplete
    @property
    def encoding(self) -> str: ...
    def copy(self) -> Request: ...
    def replace(self, *args, **kwargs) -> Request: ...
    @classmethod
    def from_curl(cls, curl_command: str, ignore_unknown_options: bool = ..., **kwargs) -> RequestTypeVar: ...
    def to_dict(self, *, spider: Optional["scrapy.Spider"] = ...) -> dict: ...
