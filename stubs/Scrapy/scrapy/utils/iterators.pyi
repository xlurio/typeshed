from _typeshed import Incomplete
from collections.abc import Generator

from scrapy.http import Response as Response, TextResponse as TextResponse
from scrapy.selector import Selector as Selector
from scrapy.utils.python import re_rsearch as re_rsearch, to_unicode as to_unicode

logger: Incomplete

def xmliter(obj, nodename) -> Generator[Incomplete, None, None]: ...
def xmliter_lxml(obj, nodename, namespace: Incomplete | None = ..., prefix: str = ...) -> Generator[Incomplete, None, None]: ...

class _StreamReader:
    def __init__(self, obj) -> None: ...
    def read(self, n: int = ...): ...

def csviter(
    obj,
    delimiter: Incomplete | None = ...,
    headers: Incomplete | None = ...,
    encoding: Incomplete | None = ...,
    quotechar: Incomplete | None = ...,
) -> Generator[Incomplete, None, Incomplete]: ...
