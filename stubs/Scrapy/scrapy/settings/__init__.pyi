from _typeshed import Incomplete
from collections.abc import Generator, MutableMapping

from scrapy.settings import default_settings as default_settings

SETTINGS_PRIORITIES: Incomplete

def get_settings_priority(priority): ...

class SettingsAttribute:
    value: Incomplete
    priority: Incomplete
    def __init__(self, value, priority) -> None: ...
    def set(self, value, priority) -> None: ...

class BaseSettings(MutableMapping):
    frozen: bool
    attributes: Incomplete
    def __init__(self, values: Incomplete | None = ..., priority: str = ...) -> None: ...
    def __getitem__(self, opt_name): ...
    def __contains__(self, name): ...
    def get(self, name, default: Incomplete | None = ...): ...
    def getbool(self, name, default: bool = ...): ...
    def getint(self, name, default: int = ...): ...
    def getfloat(self, name, default: float = ...): ...
    def getlist(self, name, default: Incomplete | None = ...): ...
    def getdict(self, name, default: Incomplete | None = ...): ...
    def getwithbase(self, name): ...
    def getpriority(self, name): ...
    def maxpriority(self): ...
    def __setitem__(self, name, value) -> None: ...
    def set(self, name, value, priority: str = ...) -> None: ...
    def setdict(self, values, priority: str = ...) -> None: ...
    def setmodule(self, module, priority: str = ...) -> None: ...
    def update(self, values, priority: str = ...) -> None: ...
    def delete(self, name, priority: str = ...) -> None: ...
    def __delitem__(self, name) -> None: ...
    def copy(self): ...
    def freeze(self) -> None: ...
    def frozencopy(self): ...
    def __iter__(self): ...
    def __len__(self): ...
    def copy_to_dict(self): ...

class _DictProxy(MutableMapping):
    o: Incomplete
    settings: Incomplete
    priority: Incomplete
    def __init__(self, settings, priority) -> None: ...
    def __len__(self): ...
    def __getitem__(self, k): ...
    def __setitem__(self, k, v) -> None: ...
    def __delitem__(self, k) -> None: ...
    def __iter__(self, k, v): ...

class Settings(BaseSettings):
    def __init__(self, values: Incomplete | None = ..., priority: str = ...) -> None: ...

def iter_default_settings() -> Generator[Incomplete, None, None]: ...
def overridden_settings(settings) -> Generator[Incomplete, None, None]: ...
