from _typeshed import Incomplete

import itemloaders
from scrapy.item import Item as Item
from scrapy.selector import Selector as Selector

class ItemLoader(itemloaders.ItemLoader):
    default_item_class: Incomplete
    default_selector_class: Incomplete
    def __init__(
        self,
        item: Incomplete | None = ...,
        selector: Incomplete | None = ...,
        response: Incomplete | None = ...,
        parent: Incomplete | None = ...,
        **context,
    ) -> None: ...
