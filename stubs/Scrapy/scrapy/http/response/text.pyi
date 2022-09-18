from _typeshed import Incomplete
from typing import Generator, Tuple

from scrapy.http import Request as Request
from scrapy.http.response import Response as Response
from scrapy.utils.python import memoizemethod_noargs as memoizemethod_noargs, to_unicode as to_unicode
from scrapy.utils.response import get_base_url as get_base_url

class TextResponse(Response):
    attributes: Tuple[str, ...]
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def encoding(self): ...
    def json(self): ...
    @property
    def text(self): ...
    def urljoin(self, url): ...
    @property
    def selector(self): ...
    def xpath(self, query, **kwargs): ...
    def css(self, query): ...
    def follow(
        self,
        url,
        callback: Incomplete | None = ...,
        method: str = ...,
        headers: Incomplete | None = ...,
        body: Incomplete | None = ...,
        cookies: Incomplete | None = ...,
        meta: Incomplete | None = ...,
        encoding: Incomplete | None = ...,
        priority: int = ...,
        dont_filter: bool = ...,
        errback: Incomplete | None = ...,
        cb_kwargs: Incomplete | None = ...,
        flags: Incomplete | None = ...,
    ) -> Request: ...
    def follow_all(
        self,
        urls: Incomplete | None = ...,
        callback: Incomplete | None = ...,
        method: str = ...,
        headers: Incomplete | None = ...,
        body: Incomplete | None = ...,
        cookies: Incomplete | None = ...,
        meta: Incomplete | None = ...,
        encoding: Incomplete | None = ...,
        priority: int = ...,
        dont_filter: bool = ...,
        errback: Incomplete | None = ...,
        cb_kwargs: Incomplete | None = ...,
        flags: Incomplete | None = ...,
        css: Incomplete | None = ...,
        xpath: Incomplete | None = ...,
    ) -> Generator[Request, None, None]: ...

class _InvalidSelector(ValueError): ...
