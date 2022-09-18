from _typeshed import Incomplete

from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning

def attribute(obj, oldattr, newattr, version: str = ...) -> None: ...
def create_deprecated_class(
    name,
    new_class,
    clsdict: Incomplete | None = ...,
    warn_category=...,
    warn_once: bool = ...,
    old_class_path: Incomplete | None = ...,
    new_class_path: Incomplete | None = ...,
    subclass_warn_message: str = ...,
    instance_warn_message: str = ...,
): ...

DEPRECATION_RULES: Incomplete

def update_classpath(path): ...
def method_is_overridden(subclass, base_class, method_name): ...
