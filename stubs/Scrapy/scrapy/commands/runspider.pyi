from _typeshed import Incomplete

from scrapy.commands import BaseRunSpiderCommand as BaseRunSpiderCommand
from scrapy.exceptions import UsageError as UsageError
from scrapy.utils.spider import iter_spider_classes as iter_spider_classes

class Command(BaseRunSpiderCommand):
    requires_project: bool
    default_settings: Incomplete
    def syntax(self): ...
    def short_desc(self): ...
    def long_desc(self): ...
    exitcode: int
    def run(self, args, opts) -> None: ...
