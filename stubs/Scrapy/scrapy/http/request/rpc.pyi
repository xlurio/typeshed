from _typeshed import Incomplete
from typing import Optional

from scrapy.http.request import Request as Request
from scrapy.utils.python import get_func_args as get_func_args

DUMPS_ARGS: Incomplete

class XmlRpcRequest(Request):
    def __init__(self, *args, encoding: Optional[str] = ..., **kwargs) -> None: ...
