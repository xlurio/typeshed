from _typeshed import Incomplete
from typing import Optional, Tuple

from scrapy.http.request import Request as Request
from scrapy.utils.deprecate import create_deprecated_class as create_deprecated_class

class JsonRequest(Request):
    attributes: Tuple[str, ...]
    def __init__(self, *args, dumps_kwargs: Optional[dict] = ..., **kwargs) -> None: ...
    @property
    def dumps_kwargs(self) -> dict: ...
    def replace(self, *args, **kwargs) -> Request: ...

JSONRequest: Incomplete
