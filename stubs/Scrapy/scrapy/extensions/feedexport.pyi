from _typeshed import Incomplete
from typing import Any, Optional, Tuple

from scrapy import Spider as Spider, signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured, ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.extensions.postprocessing import PostProcessingManager as PostProcessingManager
from scrapy.utils.boto import is_botocore_available as is_botocore_available
from scrapy.utils.conf import feed_complete_default_values_from_settings as feed_complete_default_values_from_settings
from scrapy.utils.ftp import ftp_store_file as ftp_store_file
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.python import get_func_args as get_func_args, without_none_values as without_none_values
from zope.interface import Interface

logger: Incomplete

def build_storage(builder, uri, *args, feed_options: Incomplete | None = ..., preargs=..., **kwargs): ...

class ItemFilter:
    feed_options: Optional[dict]
    item_classes: Tuple
    def __init__(self, feed_options: Optional[dict]) -> None: ...
    def accepts(self, item: Any) -> bool: ...

class IFeedStorage(Interface):
    def __init__(uri, *, feed_options: Incomplete | None = ...) -> None: ...
    def open(spider) -> None: ...
    def store(file) -> None: ...

class BlockingFeedStorage:
    def open(self, spider): ...
    def store(self, file): ...

class StdoutFeedStorage:
    def __init__(self, uri, _stdout: Incomplete | None = ..., *, feed_options: Incomplete | None = ...) -> None: ...
    def open(self, spider): ...
    def store(self, file) -> None: ...

class FileFeedStorage:
    path: Incomplete
    write_mode: Incomplete
    def __init__(self, uri, *, feed_options: Incomplete | None = ...) -> None: ...
    def open(self, spider): ...
    def store(self, file) -> None: ...

class S3FeedStorage(BlockingFeedStorage):
    bucketname: Incomplete
    access_key: Incomplete
    secret_key: Incomplete
    session_token: Incomplete
    keyname: Incomplete
    acl: Incomplete
    endpoint_url: Incomplete
    s3_client: Incomplete
    def __init__(
        self,
        uri,
        access_key: Incomplete | None = ...,
        secret_key: Incomplete | None = ...,
        acl: Incomplete | None = ...,
        endpoint_url: Incomplete | None = ...,
        *,
        feed_options: Incomplete | None = ...,
        session_token: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def from_crawler(cls, crawler, uri, *, feed_options: Incomplete | None = ...): ...

class GCSFeedStorage(BlockingFeedStorage):
    project_id: Incomplete
    acl: Incomplete
    bucket_name: Incomplete
    blob_name: Incomplete
    def __init__(self, uri, project_id, acl) -> None: ...
    @classmethod
    def from_crawler(cls, crawler, uri): ...

class FTPFeedStorage(BlockingFeedStorage):
    host: Incomplete
    port: Incomplete
    username: Incomplete
    password: Incomplete
    path: Incomplete
    use_active_mode: Incomplete
    overwrite: Incomplete
    def __init__(self, uri, use_active_mode: bool = ..., *, feed_options: Incomplete | None = ...) -> None: ...
    @classmethod
    def from_crawler(cls, crawler, uri, *, feed_options: Incomplete | None = ...): ...

class _FeedSlot:
    file: Incomplete
    exporter: Incomplete
    storage: Incomplete
    batch_id: Incomplete
    format: Incomplete
    store_empty: Incomplete
    uri_template: Incomplete
    uri: Incomplete
    filter: Incomplete
    itemcount: int
    def __init__(self, file, exporter, storage, uri, format, store_empty, batch_id, uri_template, filter) -> None: ...
    def start_exporting(self) -> None: ...
    def finish_exporting(self) -> None: ...

class FeedExporter:
    @classmethod
    def from_crawler(cls, crawler): ...
    crawler: Incomplete
    settings: Incomplete
    feeds: Incomplete
    slots: Incomplete
    filters: Incomplete
    storages: Incomplete
    exporters: Incomplete
    def __init__(self, crawler) -> None: ...
    def open_spider(self, spider) -> None: ...
    def close_spider(self, spider): ...
    def item_scraped(self, item, spider) -> None: ...
