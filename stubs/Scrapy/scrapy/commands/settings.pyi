from _typeshed import Incomplete

from scrapy.commands import ScrapyCommand as ScrapyCommand
from scrapy.settings import BaseSettings as BaseSettings

class Command(ScrapyCommand):
    requires_project: bool
    default_settings: Incomplete
    def syntax(self): ...
    def short_desc(self): ...
    def add_options(self, parser) -> None: ...
    def run(self, args, opts) -> None: ...
