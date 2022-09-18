from typing import Optional

import scrapy
from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning

def request_to_dict(request: scrapy.Request, spider: Optional["scrapy.Spider"] = ...) -> dict: ...
def request_from_dict(d: dict, spider: Optional["scrapy.Spider"] = ...) -> scrapy.Request: ...
