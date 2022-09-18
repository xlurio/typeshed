from _typeshed import Incomplete

class Link:
    url: Incomplete
    text: Incomplete
    fragment: Incomplete
    nofollow: Incomplete
    def __init__(self, url, text: str = ..., fragment: str = ..., nofollow: bool = ...) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
