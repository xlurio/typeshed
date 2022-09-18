from _typeshed import Incomplete

from scrapy.utils.deprecate import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.utils.misc import arg_to_iter as arg_to_iter
from scrapy.utils.url import url_has_any_extension as url_has_any_extension, url_is_from_any_domain as url_is_from_any_domain

IGNORED_EXTENSIONS: Incomplete

class FilteringLinkExtractor:
    def __new__(cls, *args, **kwargs): ...
    link_extractor: Incomplete
    allow_res: Incomplete
    deny_res: Incomplete
    allow_domains: Incomplete
    deny_domains: Incomplete
    restrict_xpaths: Incomplete
    canonicalize: Incomplete
    deny_extensions: Incomplete
    restrict_text: Incomplete
    def __init__(
        self,
        link_extractor,
        allow,
        deny,
        allow_domains,
        deny_domains,
        restrict_xpaths,
        canonicalize,
        deny_extensions,
        restrict_css,
        restrict_text,
    ) -> None: ...
    def matches(self, url): ...
