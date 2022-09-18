from _typeshed import Incomplete

from scrapy.exceptions import IgnoreRequest as IgnoreRequest, NotConfigured as NotConfigured
from scrapy.http import Request as Request
from scrapy.pipelines.media import MediaPipeline as MediaPipeline
from scrapy.settings import Settings as Settings
from scrapy.utils.boto import is_botocore_available as is_botocore_available
from scrapy.utils.datatypes import CaselessDict as CaselessDict
from scrapy.utils.ftp import ftp_store_file as ftp_store_file
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info
from scrapy.utils.misc import md5sum as md5sum
from scrapy.utils.python import to_bytes as to_bytes
from scrapy.utils.request import referer_str as referer_str

logger: Incomplete

class FileException(Exception): ...

class FSFilesStore:
    basedir: Incomplete
    created_directories: Incomplete
    def __init__(self, basedir) -> None: ...
    def persist_file(self, path, buf, info, meta: Incomplete | None = ..., headers: Incomplete | None = ...) -> None: ...
    def stat_file(self, path, info): ...

class S3FilesStore:
    AWS_ACCESS_KEY_ID: Incomplete
    AWS_SECRET_ACCESS_KEY: Incomplete
    AWS_SESSION_TOKEN: Incomplete
    AWS_ENDPOINT_URL: Incomplete
    AWS_REGION_NAME: Incomplete
    AWS_USE_SSL: Incomplete
    AWS_VERIFY: Incomplete
    POLICY: str
    HEADERS: Incomplete
    s3_client: Incomplete
    def __init__(self, uri) -> None: ...
    def stat_file(self, path, info): ...
    def persist_file(self, path, buf, info, meta: Incomplete | None = ..., headers: Incomplete | None = ...): ...

class GCSFilesStore:
    GCS_PROJECT_ID: Incomplete
    CACHE_CONTROL: str
    POLICY: Incomplete
    bucket: Incomplete
    prefix: Incomplete
    def __init__(self, uri) -> None: ...
    def stat_file(self, path, info): ...
    def persist_file(self, path, buf, info, meta: Incomplete | None = ..., headers: Incomplete | None = ...): ...

class FTPFilesStore:
    FTP_USERNAME: Incomplete
    FTP_PASSWORD: Incomplete
    USE_ACTIVE_MODE: Incomplete
    port: Incomplete
    host: Incomplete
    username: Incomplete
    password: Incomplete
    basedir: Incomplete
    def __init__(self, uri) -> None: ...
    def persist_file(self, path, buf, info, meta: Incomplete | None = ..., headers: Incomplete | None = ...): ...
    def stat_file(self, path, info): ...

class FilesPipeline(MediaPipeline):
    MEDIA_NAME: str
    EXPIRES: int
    STORE_SCHEMES: Incomplete
    DEFAULT_FILES_URLS_FIELD: str
    DEFAULT_FILES_RESULT_FIELD: str
    store: Incomplete
    expires: Incomplete
    FILES_URLS_FIELD: Incomplete
    FILES_RESULT_FIELD: Incomplete
    files_urls_field: Incomplete
    files_result_field: Incomplete
    def __init__(self, store_uri, download_func: Incomplete | None = ..., settings: Incomplete | None = ...) -> None: ...
    @classmethod
    def from_settings(cls, settings): ...
    def media_to_download(self, request, info, *, item: Incomplete | None = ...): ...
    def media_failed(self, failure, request, info) -> None: ...
    def media_downloaded(self, response, request, info, *, item: Incomplete | None = ...): ...
    def inc_stats(self, spider, status) -> None: ...
    def get_media_requests(self, item, info): ...
    def file_downloaded(self, response, request, info, *, item: Incomplete | None = ...): ...
    def item_completed(self, results, item, info): ...
    def file_path(
        self, request, response: Incomplete | None = ..., info: Incomplete | None = ..., *, item: Incomplete | None = ...
    ): ...
