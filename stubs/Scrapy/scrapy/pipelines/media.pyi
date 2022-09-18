from _typeshed import Incomplete

from scrapy.settings import Settings as Settings
from scrapy.utils.datatypes import SequenceExclude as SequenceExclude
from scrapy.utils.defer import defer_result as defer_result, mustbe_deferred as mustbe_deferred
from scrapy.utils.deprecate import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info
from scrapy.utils.misc import arg_to_iter as arg_to_iter
from scrapy.utils.request import request_fingerprint as request_fingerprint

logger: Incomplete

class MediaPipeline:
    LOG_FAILED_RESULTS: bool

    class SpiderInfo:
        spider: Incomplete
        downloading: Incomplete
        downloaded: Incomplete
        waiting: Incomplete
        def __init__(self, spider) -> None: ...
    download_func: Incomplete
    allow_redirects: Incomplete
    def __init__(self, download_func: Incomplete | None = ..., settings: Incomplete | None = ...) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    spiderinfo: Incomplete
    def open_spider(self, spider) -> None: ...
    def process_item(self, item, spider): ...
    def media_to_download(self, request, info, *, item: Incomplete | None = ...) -> None: ...
    def get_media_requests(self, item, info) -> None: ...
    def media_downloaded(self, response, request, info, *, item: Incomplete | None = ...): ...
    def media_failed(self, failure, request, info): ...
    def item_completed(self, results, item, info): ...
    def file_path(
        self, request, response: Incomplete | None = ..., info: Incomplete | None = ..., *, item: Incomplete | None = ...
    ) -> None: ...
