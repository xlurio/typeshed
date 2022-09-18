from _typeshed import Incomplete

from twisted.internet import protocol

class ProcessTest:
    command: Incomplete
    prefix: Incomplete
    cwd: Incomplete
    def execute(self, args, check_code: bool = ..., settings: Incomplete | None = ...): ...

class TestProcessProtocol(protocol.ProcessProtocol):
    deferred: Incomplete
    out: bytes
    err: bytes
    exitcode: Incomplete
    def __init__(self) -> None: ...
    def outReceived(self, data) -> None: ...
    def errReceived(self, data) -> None: ...
    def processEnded(self, status) -> None: ...
