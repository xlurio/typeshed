from _typeshed import Incomplete

from scrapy.commands import ScrapyCommand as ScrapyCommand
from scrapy.http import Request as Request
from scrapy.shell import Shell as Shell
from scrapy.utils.spider import DefaultSpider as DefaultSpider, spidercls_for_request as spidercls_for_request
from scrapy.utils.url import guess_scheme as guess_scheme

class Command(ScrapyCommand):
    requires_project: bool
    default_settings: Incomplete
    def syntax(self): ...
    def short_desc(self): ...
    def long_desc(self): ...
    def add_options(self, parser) -> None: ...
    def update_vars(self, vars) -> None: ...
    def run(self, args, opts) -> None: ...
