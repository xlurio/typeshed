from _typeshed import Incomplete

from scrapy.utils.ssl import get_temp_key_info as get_temp_key_info, x509name_to_string as x509name_to_string
from twisted.internet._sslverify import ClientTLSOptions

logger: Incomplete
METHOD_SSLv3: str
METHOD_TLS: str
METHOD_TLSv10: str
METHOD_TLSv11: str
METHOD_TLSv12: str
openssl_methods: Incomplete

class ScrapyClientTLSOptions(ClientTLSOptions):
    verbose_logging: Incomplete
    def __init__(self, hostname, ctx, verbose_logging: bool = ...) -> None: ...

DEFAULT_CIPHERS: Incomplete
