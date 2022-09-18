import json

from scrapy.http import Request as Request, Response as Response

class ScrapyJSONEncoder(json.JSONEncoder):
    DATE_FORMAT: str
    TIME_FORMAT: str
    def default(self, o): ...

class ScrapyJSONDecoder(json.JSONDecoder): ...
