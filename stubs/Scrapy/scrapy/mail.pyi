from _typeshed import Incomplete

from scrapy.utils.misc import arg_to_iter as arg_to_iter
from scrapy.utils.python import to_bytes as to_bytes

logger: Incomplete
COMMASPACE: str

class MailSender:
    smtphost: Incomplete
    smtpport: Incomplete
    smtpuser: Incomplete
    smtppass: Incomplete
    smtptls: Incomplete
    smtpssl: Incomplete
    mailfrom: Incomplete
    debug: Incomplete
    def __init__(
        self,
        smtphost: str = ...,
        mailfrom: str = ...,
        smtpuser: Incomplete | None = ...,
        smtppass: Incomplete | None = ...,
        smtpport: int = ...,
        smtptls: bool = ...,
        smtpssl: bool = ...,
        debug: bool = ...,
    ) -> None: ...
    @classmethod
    def from_settings(cls, settings): ...
    def send(
        self,
        to,
        subject,
        body,
        cc: Incomplete | None = ...,
        attachs=...,
        mimetype: str = ...,
        charset: Incomplete | None = ...,
        _callback: Incomplete | None = ...,
    ): ...
