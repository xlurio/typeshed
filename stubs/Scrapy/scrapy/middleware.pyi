from _typeshed import Incomplete

from scrapy import Spider as Spider
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.settings import Settings as Settings
from scrapy.utils.defer import process_chain as process_chain, process_parallel as process_parallel
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from twisted.internet.defer import Deferred as Deferred

logger: Incomplete

class MiddlewareManager:
    component_name: str
    middlewares: Incomplete
    methods: Incomplete
    def __init__(self, *middlewares) -> None: ...
    @classmethod
    def from_settings(cls, settings: Settings, crawler: Incomplete | None = ...): ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def open_spider(self, spider: Spider) -> Deferred: ...
    def close_spider(self, spider: Spider) -> Deferred: ...
