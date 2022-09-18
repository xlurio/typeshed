from _typeshed import Incomplete
from typing import Optional, Tuple

from scrapy.core.downloader.contextfactory import AcceptableProtocolsContextFactory as AcceptableProtocolsContextFactory
from scrapy.core.http2.protocol import H2ClientFactory as H2ClientFactory, H2ClientProtocol as H2ClientProtocol
from scrapy.http.request import Request as Request
from scrapy.settings import Settings as Settings
from scrapy.spiders import Spider as Spider
from twisted.internet.base import ReactorBase as ReactorBase
from twisted.internet.defer import Deferred
from twisted.internet.endpoints import HostnameEndpoint as HostnameEndpoint
from twisted.web.client import URI, BrowserLikePolicyForHTTPS

class H2ConnectionPool:
    settings: Incomplete
    def __init__(self, reactor: ReactorBase, settings: Settings) -> None: ...
    def get_connection(self, key: Tuple, uri: URI, endpoint: HostnameEndpoint) -> Deferred: ...
    def put_connection(self, conn: H2ClientProtocol, key: Tuple) -> H2ClientProtocol: ...
    def close_connections(self) -> None: ...

class H2Agent:
    endpoint_factory: Incomplete
    def __init__(
        self,
        reactor: ReactorBase,
        pool: H2ConnectionPool,
        context_factory: BrowserLikePolicyForHTTPS = ...,
        connect_timeout: Optional[float] = ...,
        bind_address: Optional[bytes] = ...,
    ) -> None: ...
    def get_endpoint(self, uri: URI): ...
    def get_key(self, uri: URI) -> Tuple: ...
    def request(self, request: Request, spider: Spider) -> Deferred: ...

class ScrapyProxyH2Agent(H2Agent):
    def __init__(
        self,
        reactor: ReactorBase,
        proxy_uri: URI,
        pool: H2ConnectionPool,
        context_factory: BrowserLikePolicyForHTTPS = ...,
        connect_timeout: Optional[float] = ...,
        bind_address: Optional[bytes] = ...,
    ) -> None: ...
    def get_endpoint(self, uri: URI): ...
    def get_key(self, uri: URI) -> Tuple: ...
