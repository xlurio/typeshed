from _typeshed import Incomplete

from scrapy.crawler import Crawler as Crawler
from scrapy.exceptions import IgnoreRequest as IgnoreRequest
from scrapy.http import Request as Request, Response as Response
from scrapy.settings import Settings as Settings
from scrapy.spiders import Spider as Spider
from scrapy.utils.conf import get_config as get_config
from scrapy.utils.console import DEFAULT_PYTHON_SHELLS as DEFAULT_PYTHON_SHELLS, start_python_console as start_python_console
from scrapy.utils.datatypes import SequenceExclude as SequenceExclude
from scrapy.utils.misc import load_object as load_object
from scrapy.utils.response import open_in_browser as open_in_browser

class Shell:
    relevant_classes: Incomplete
    crawler: Incomplete
    update_vars: Incomplete
    item_class: Incomplete
    spider: Incomplete
    inthread: Incomplete
    code: Incomplete
    vars: Incomplete
    def __init__(self, crawler, update_vars: Incomplete | None = ..., code: Incomplete | None = ...) -> None: ...
    def start(
        self,
        url: Incomplete | None = ...,
        request: Incomplete | None = ...,
        response: Incomplete | None = ...,
        spider: Incomplete | None = ...,
        redirect: bool = ...,
    ) -> None: ...
    def fetch(self, request_or_url, spider: Incomplete | None = ..., redirect: bool = ..., **kwargs) -> None: ...
    def populate_vars(
        self, response: Incomplete | None = ..., request: Incomplete | None = ..., spider: Incomplete | None = ...
    ) -> None: ...
    def print_help(self) -> None: ...
    def get_help(self): ...

def inspect_response(response, spider) -> None: ...
