from _typeshed import Incomplete

from scrapy.exceptions import StopDownload as StopDownload
from scrapy.utils.defer import maybeDeferred_coro as maybeDeferred_coro
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info

logger: Incomplete

def send_catch_log(signal=..., sender=..., *arguments, **named): ...
def send_catch_log_deferred(signal=..., sender=..., *arguments, **named): ...
def disconnect_all(signal=..., sender=...) -> None: ...
