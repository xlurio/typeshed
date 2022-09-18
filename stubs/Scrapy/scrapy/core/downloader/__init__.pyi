from _typeshed import Incomplete

from scrapy import signals as signals
from scrapy.core.downloader.handlers import DownloadHandlers as DownloadHandlers
from scrapy.core.downloader.middleware import DownloaderMiddlewareManager as DownloaderMiddlewareManager
from scrapy.resolver import dnscache as dnscache
from scrapy.utils.defer import mustbe_deferred as mustbe_deferred
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached

class Slot:
    concurrency: Incomplete
    delay: Incomplete
    randomize_delay: Incomplete
    active: Incomplete
    queue: Incomplete
    transferring: Incomplete
    lastseen: int
    latercall: Incomplete
    def __init__(self, concurrency, delay, randomize_delay) -> None: ...
    def free_transfer_slots(self): ...
    def download_delay(self): ...
    def close(self) -> None: ...

class Downloader:
    DOWNLOAD_SLOT: str
    settings: Incomplete
    signals: Incomplete
    slots: Incomplete
    active: Incomplete
    handlers: Incomplete
    total_concurrency: Incomplete
    domain_concurrency: Incomplete
    ip_concurrency: Incomplete
    randomize_delay: Incomplete
    middleware: Incomplete
    def __init__(self, crawler) -> None: ...
    def fetch(self, request, spider): ...
    def needs_backout(self): ...
    def close(self) -> None: ...
