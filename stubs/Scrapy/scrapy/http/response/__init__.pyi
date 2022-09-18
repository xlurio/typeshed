from _typeshed import Incomplete
from typing import Generator, Tuple

from scrapy.exceptions import NotSupported as NotSupported
from scrapy.http.common import obsolete_setter as obsolete_setter
from scrapy.http.headers import Headers as Headers
from scrapy.http.request import Request as Request
from scrapy.link import Link as Link
from scrapy.utils.trackref import object_ref as object_ref

class Response(object_ref):
    attributes: Tuple[str, ...]
    headers: Incomplete
    status: Incomplete
    request: Incomplete
    flags: Incomplete
    certificate: Incomplete
    ip_address: Incomplete
    protocol: Incomplete
    def __init__(
        self,
        url,
        status: int = ...,
        headers: Incomplete | None = ...,
        body: bytes = ...,
        flags: Incomplete | None = ...,
        request: Incomplete | None = ...,
        certificate: Incomplete | None = ...,
        ip_address: Incomplete | None = ...,
        protocol: Incomplete | None = ...,
    ) -> None: ...
    @property
    def cb_kwargs(self): ...
    @property
    def meta(self): ...
    url: Incomplete
    body: Incomplete
    def copy(self): ...
    def replace(self, *args, **kwargs): ...
    def urljoin(self, url): ...
    @property
    def text(self) -> None: ...
    def css(self, *a, **kw) -> None: ...
    def xpath(self, *a, **kw) -> None: ...
    def follow(
        self,
        url,
        callback: Incomplete | None = ...,
        method: str = ...,
        headers: Incomplete | None = ...,
        body: Incomplete | None = ...,
        cookies: Incomplete | None = ...,
        meta: Incomplete | None = ...,
        encoding: str = ...,
        priority: int = ...,
        dont_filter: bool = ...,
        errback: Incomplete | None = ...,
        cb_kwargs: Incomplete | None = ...,
        flags: Incomplete | None = ...,
    ) -> Request: ...
    def follow_all(
        self,
        urls,
        callback: Incomplete | None = ...,
        method: str = ...,
        headers: Incomplete | None = ...,
        body: Incomplete | None = ...,
        cookies: Incomplete | None = ...,
        meta: Incomplete | None = ...,
        encoding: str = ...,
        priority: int = ...,
        dont_filter: bool = ...,
        errback: Incomplete | None = ...,
        cb_kwargs: Incomplete | None = ...,
        flags: Incomplete | None = ...,
    ) -> Generator[Request, None, None]: ...
