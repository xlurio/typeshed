from _typeshed import Incomplete
from collections.abc import Generator

import scrapy
from scrapy.commands import ScrapyCommand as ScrapyCommand
from scrapy.linkextractors import LinkExtractor as LinkExtractor

class Command(ScrapyCommand):
    default_settings: Incomplete
    def short_desc(self): ...
    def run(self, args, opts) -> None: ...

class _BenchServer:
    proc: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class _BenchSpider(scrapy.Spider):
    name: str
    total: int
    show: int
    baseurl: str
    link_extractor: Incomplete
    def start_requests(self): ...
    def parse(self, response) -> Generator[Incomplete, None, None]: ...
