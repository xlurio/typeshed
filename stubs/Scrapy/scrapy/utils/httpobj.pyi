from typing import Union
from urllib.parse import ParseResult as ParseResult

from scrapy.http import Request as Request, Response as Response

def urlparse_cached(request_or_response: Union[Request, Response]) -> ParseResult: ...
