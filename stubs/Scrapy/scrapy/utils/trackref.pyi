from _typeshed import Incomplete
from typing import DefaultDict
from weakref import WeakKeyDictionary

NoneType: Incomplete
live_refs: DefaultDict[type, WeakKeyDictionary]

class object_ref:
    def __new__(cls, *args, **kwargs): ...

def format_live_refs(ignore=...): ...
def print_live_refs(*a, **kw) -> None: ...
def get_oldest(class_name): ...
def iter_all(class_name): ...
