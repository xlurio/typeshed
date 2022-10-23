from _typeshed import Incomplete
from io import TextIOWrapper
from types import MappingProxyType
from typing import BinaryIO, Generator, Protocol, TextIO
from pydantic import BaseModel
from scrapy.utils.serialize import ScrapyJSONEncoder
from xml.sax.saxutils import XMLGenerator
from _csv import _writer

class IsDataclass(Protocol):
    __dataclass_fields__: dict[object, object]

class IsAttrs(Protocol):
    __attrs_attrs__: Incomplete

class BaseItemExporter:
    def __init__(self, *, dont_fail: bool = ..., **kwargs: object) -> None: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...
    def serialize_field(
        self, field: MappingProxyType[str, object], name: str, value: object
    ) -> Generator[tuple[str | object], None, None]: ...
    def start_exporting(self) -> None: ...
    def finish_exporting(self) -> None: ...

class JsonLinesItemExporter(BaseItemExporter):
    file: BinaryIO
    encoder: ScrapyJSONEncoder
    def __init__(self, file: BinaryIO, **kwargs: object) -> None: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...

class JsonItemExporter(BaseItemExporter):
    file: BinaryIO
    encoder: ScrapyJSONEncoder
    first_item: bool
    def __init__(self, file: BinaryIO, **kwargs: object) -> None: ...
    def start_exporting(self) -> None: ...
    def finish_exporting(self) -> None: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...

class XmlItemExporter(BaseItemExporter):
    item_element: str
    root_element: str
    encoding: str
    xg: XMLGenerator
    def __init__(self, file: TextIO | BinaryIO, **kwargs: object) -> None: ...
    def start_exporting(self) -> None: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...
    def finish_exporting(self) -> None: ...

class CsvItemExporter(BaseItemExporter):
    encoding: str
    include_headers_line: bool
    stream: TextIOWrapper
    csv_writer: _writer
    def __init__(
        self,
        file: TextIO,
        include_headers_line: bool = ...,
        join_multivalued: str = ...,
        errors: str | None = ...,
        **kwargs: object,
    ) -> None: ...
    def serialize_field(
        self, field: MappingProxyType[str, object], name: str, value: object
    ) -> Generator[tuple[str | object], None, None]: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...

class PickleItemExporter(BaseItemExporter):
    file: TextIO | BinaryIO
    protocol: int
    def __init__(self, file: TextIO | BinaryIO, protocol: int = ..., **kwargs: object) -> None: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...

class MarshalItemExporter(BaseItemExporter):
    file: BinaryIO
    def __init__(self, file: BinaryIO, **kwargs: object) -> None: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...

class PprintItemExporter(BaseItemExporter):
    file: BinaryIO
    def __init__(self, file: BinaryIO, **kwargs: object) -> None: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...

class PythonItemExporter(BaseItemExporter):
    def serialize_field(
        self, field: MappingProxyType[str, object], name: str, value: object
    ) -> Generator[tuple[str | object], None, None]: ...
    def export_item(self, item: tuple[object] | dict[str, object] | BaseModel | IsDataclass) -> None: ...
