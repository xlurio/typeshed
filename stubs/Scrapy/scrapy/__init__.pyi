def __getattr__(name: str): ...  # incomplete

from scrapy.http import FormRequest as FormRequest, Request as Request
from scrapy.item import Field as Field, Item as Item
from scrapy.selector import Selector as Selector
from scrapy.spiders import Spider as Spider

version_info: tuple[int]
twisted_version: tuple[int]

# Names in __all__ with no definition:
#   __version__
