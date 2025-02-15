from _typeshed import Incomplete

from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.python import to_unicode as to_unicode

IPV4_RE: Incomplete

class CookieJar:
    policy: Incomplete
    jar: Incomplete
    check_expired_frequency: Incomplete
    processed: int
    def __init__(self, policy: Incomplete | None = ..., check_expired_frequency: int = ...) -> None: ...
    def extract_cookies(self, response, request): ...
    def add_cookie_header(self, request) -> None: ...
    def clear_session_cookies(self, *args, **kwargs): ...
    def clear(self, domain: Incomplete | None = ..., path: Incomplete | None = ..., name: Incomplete | None = ...): ...
    def __iter__(self): ...
    def __len__(self): ...
    def set_policy(self, pol): ...
    def make_cookies(self, response, request): ...
    def set_cookie(self, cookie) -> None: ...
    def set_cookie_if_ok(self, cookie, request) -> None: ...

def potential_domain_matches(domain): ...

class _DummyLock:
    def acquire(self) -> None: ...
    def release(self) -> None: ...

class WrappedRequest:
    request: Incomplete
    def __init__(self, request) -> None: ...
    def get_full_url(self): ...
    def get_host(self): ...
    def get_type(self): ...
    def is_unverifiable(self): ...
    @property
    def full_url(self): ...
    @property
    def host(self): ...
    @property
    def type(self): ...
    @property
    def unverifiable(self): ...
    @property
    def origin_req_host(self): ...
    def has_header(self, name): ...
    def get_header(self, name, default: Incomplete | None = ...): ...
    def header_items(self): ...
    def add_unredirected_header(self, name, value) -> None: ...

class WrappedResponse:
    response: Incomplete
    def __init__(self, response) -> None: ...
    def info(self): ...
    def get_all(self, name, default: Incomplete | None = ...): ...
