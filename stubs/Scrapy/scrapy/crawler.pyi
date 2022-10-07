from logging import Logger
from typing import Iterable, Iterator, Type

from scrapy import Spider as Spider, signals as signals
from scrapy.statscollectors import StatsCollector
from scrapy.logformatter import LogFormatter
from scrapy.core.engine import ExecutionEngine as ExecutionEngine
from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.extension import ExtensionManager as ExtensionManager
from scrapy.interfaces import ISpiderLoader as ISpiderLoader
from scrapy.settings import Settings as Settings, overridden_settings as overridden_settings
from scrapy.signalmanager import SignalManager as SignalManager
from scrapy.utils.log import (
    LogCounterHandler as LogCounterHandler,
    configure_logging as configure_logging,
    get_scrapy_root_handler as get_scrapy_root_handler,
    install_scrapy_root_handler as install_scrapy_root_handler,
    log_reactor_info as log_reactor_info,
    log_scrapy_info as log_scrapy_info,
)
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.ossignal import install_shutdown_handlers as install_shutdown_handlers, signal_names as signal_names
from scrapy.utils.reactor import install_reactor as install_reactor, verify_installed_reactor as verify_installed_reactor
from twisted.internet.defer import Deferred, DeferredList

logger: Logger

class Crawler:
    spidercls: Type[Spider]
    settings: Settings
    signals: SignalManager
    stats: StatsCollector
    logformatter: LogFormatter
    extensions: ExtensionManager
    crawling: bool
    spider: Spider | None
    engine: ExecutionEngine | None
    def __init__(self, spidercls: Type[Spider], settings: Settings | dict[str, object] | None = ..., init_reactor: bool = ...) -> None: ...
    def crawl(self, *args: object, **kwargs: object) -> Iterator[dict[str, object]]: ...
    def stop(self) -> Iterator[Deferred[None]]: ...

class CrawlerRunner:
    crawlers: set[Crawler]
    settings: Settings
    spider_loader: ISpiderLoader
    bootstrap_failed: bool
    def __init__(self, settings: Settings | dict[str, object] | None = ...) -> None: ...
    @property
    def spiders(self) -> ISpiderLoader: ...
    def crawl(self, crawler_or_spidercls: Crawler | Type[Spider] | Spider, *args: object, **kwargs: object) -> Deferred[Iterable[dict[str, object]]]: ...
    def create_crawler(self, crawler_or_spidercls: Crawler | Type[Spider] | Spider) -> Crawler: ...
    def stop(self) -> DeferredList: ...
    def join(self) -> DeferredList: ...

class CrawlerProcess(CrawlerRunner):
    def __init__(self, settings: Settings | dict[str, object] | None = ..., install_root_handler: bool = ...) -> None: ...
    def start(self, stop_after_crawl: bool = ..., install_signal_handlers: bool = ...) -> None: ...
