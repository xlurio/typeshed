from _typeshed import Incomplete

from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured, NotSupported as NotSupported
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.python import without_none_values as without_none_values

logger: Incomplete

class DownloadHandlers:
    def __init__(self, crawler) -> None: ...
    def download_request(self, request, spider): ...
