from _typeshed import Incomplete

from scrapy.core.downloader.tls import (
    DEFAULT_CIPHERS as DEFAULT_CIPHERS,
    ScrapyClientTLSOptions as ScrapyClientTLSOptions,
    openssl_methods as openssl_methods,
)
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from twisted.web.client import BrowserLikePolicyForHTTPS

class ScrapyClientContextFactory(BrowserLikePolicyForHTTPS):
    tls_verbose_logging: Incomplete
    tls_ciphers: Incomplete
    def __init__(
        self, method=..., tls_verbose_logging: bool = ..., tls_ciphers: Incomplete | None = ..., *args, **kwargs
    ) -> None: ...
    @classmethod
    def from_settings(cls, settings, method=..., *args, **kwargs): ...
    def getCertificateOptions(self): ...
    def getContext(self, hostname: Incomplete | None = ..., port: Incomplete | None = ...): ...
    def creatorForNetloc(self, hostname, port): ...

class BrowserLikeContextFactory(ScrapyClientContextFactory):
    def creatorForNetloc(self, hostname, port): ...

class AcceptableProtocolsContextFactory:
    def __init__(self, context_factory, acceptable_protocols) -> None: ...
    def creatorForNetloc(self, hostname, port): ...

def load_context_factory_from_settings(settings, crawler): ...
