from _typeshed import Incomplete

from scrapy import signals as signals
from scrapy.core.downloader.contextfactory import load_context_factory_from_settings as load_context_factory_from_settings
from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning, StopDownload as StopDownload
from scrapy.http import Headers as Headers
from scrapy.responsetypes import responsetypes as responsetypes
from scrapy.utils.python import to_bytes as to_bytes, to_unicode as to_unicode
from twisted.internet import protocol
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.web.client import Agent

logger: Incomplete

class HTTP11DownloadHandler:
    lazy: bool
    def __init__(self, settings, crawler: Incomplete | None = ...) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def download_request(self, request, spider): ...
    def close(self): ...

class TunnelError(Exception): ...

class TunnelingTCP4ClientEndpoint(TCP4ClientEndpoint):
    def __init__(
        self, reactor, host, port, proxyConf, contextFactory, timeout: int = ..., bindAddress: Incomplete | None = ...
    ) -> None: ...
    def requestTunnel(self, protocol): ...
    def processProxyResponse(self, rcvd_bytes) -> None: ...
    def connectFailed(self, reason) -> None: ...
    def connect(self, protocolFactory): ...

def tunnel_request_data(host, port, proxy_auth_header: Incomplete | None = ...): ...

class TunnelingAgent(Agent):
    def __init__(
        self,
        reactor,
        proxyConf,
        contextFactory: Incomplete | None = ...,
        connectTimeout: Incomplete | None = ...,
        bindAddress: Incomplete | None = ...,
        pool: Incomplete | None = ...,
    ) -> None: ...

class ScrapyProxyAgent(Agent):
    def __init__(
        self,
        reactor,
        proxyURI,
        connectTimeout: Incomplete | None = ...,
        bindAddress: Incomplete | None = ...,
        pool: Incomplete | None = ...,
    ) -> None: ...
    def request(self, method, uri, headers: Incomplete | None = ..., bodyProducer: Incomplete | None = ...): ...

class ScrapyAgent:
    def __init__(
        self,
        contextFactory: Incomplete | None = ...,
        connectTimeout: int = ...,
        bindAddress: Incomplete | None = ...,
        pool: Incomplete | None = ...,
        maxsize: int = ...,
        warnsize: int = ...,
        fail_on_dataloss: bool = ...,
        crawler: Incomplete | None = ...,
    ) -> None: ...
    def download_request(self, request): ...

class _RequestBodyProducer:
    body: Incomplete
    length: Incomplete
    def __init__(self, body) -> None: ...
    def startProducing(self, consumer): ...
    def pauseProducing(self) -> None: ...
    def stopProducing(self) -> None: ...

class _ResponseReader(protocol.Protocol):
    def __init__(self, finished, txresponse, request, maxsize, warnsize, fail_on_dataloss, crawler) -> None: ...
    def connectionMade(self) -> None: ...
    def dataReceived(self, bodyBytes) -> None: ...
    def connectionLost(self, reason) -> None: ...
