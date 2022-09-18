from _typeshed import Incomplete

from parsel import Selector as _ParselSelector
from scrapy.utils.trackref import object_ref

class SelectorList(_ParselSelector.selectorlist_cls, object_ref): ...

class Selector(_ParselSelector, object_ref):
    selectorlist_cls: Incomplete
    response: Incomplete
    def __init__(
        self,
        response: Incomplete | None = ...,
        text: Incomplete | None = ...,
        type: Incomplete | None = ...,
        root: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...
