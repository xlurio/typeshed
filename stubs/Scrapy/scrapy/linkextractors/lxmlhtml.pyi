from _typeshed import Incomplete

from scrapy.link import Link as Link
from scrapy.linkextractors import FilteringLinkExtractor as FilteringLinkExtractor
from scrapy.utils.misc import arg_to_iter as arg_to_iter, rel_has_nofollow as rel_has_nofollow
from scrapy.utils.response import get_base_url as get_base_url

XHTML_NAMESPACE: str

class LxmlParserLinkExtractor:
    scan_tag: Incomplete
    scan_attr: Incomplete
    process_attr: Incomplete
    unique: Incomplete
    strip: Incomplete
    link_key: Incomplete
    def __init__(
        self,
        tag: str = ...,
        attr: str = ...,
        process: Incomplete | None = ...,
        unique: bool = ...,
        strip: bool = ...,
        canonicalized: bool = ...,
    ) -> None: ...
    def extract_links(self, response): ...

class LxmlLinkExtractor(FilteringLinkExtractor):
    def __init__(
        self,
        allow=...,
        deny=...,
        allow_domains=...,
        deny_domains=...,
        restrict_xpaths=...,
        tags=...,
        attrs=...,
        canonicalize: bool = ...,
        unique: bool = ...,
        process_value: Incomplete | None = ...,
        deny_extensions: Incomplete | None = ...,
        restrict_css=...,
        strip: bool = ...,
        restrict_text: Incomplete | None = ...,
    ) -> None: ...
    def extract_links(self, response): ...
