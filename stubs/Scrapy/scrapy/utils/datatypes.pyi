import collections
import weakref
from _typeshed import Incomplete

class CaselessDict(dict):
    def __init__(self, seq: Incomplete | None = ...) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key): ...
    has_key: Incomplete
    def __copy__(self): ...
    copy: Incomplete
    def normkey(self, key): ...
    def normvalue(self, value): ...
    def get(self, key, def_val: Incomplete | None = ...): ...
    def setdefault(self, key, def_val: Incomplete | None = ...): ...
    def update(self, seq) -> None: ...
    @classmethod
    def fromkeys(cls, keys, value: Incomplete | None = ...): ...
    def pop(self, key, *args): ...

class LocalCache(collections.OrderedDict):
    limit: Incomplete
    def __init__(self, limit: Incomplete | None = ...) -> None: ...
    def __setitem__(self, key, value) -> None: ...

class LocalWeakReferencedCache(weakref.WeakKeyDictionary):
    data: Incomplete
    def __init__(self, limit: Incomplete | None = ...) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def __getitem__(self, key): ...

class SequenceExclude:
    seq: Incomplete
    def __init__(self, seq) -> None: ...
    def __contains__(self, item): ...
