from _typeshed import Incomplete
from typing import List, Optional, Tuple, TypeVar, Union

from lxml.html import FormElement as FormElement, HtmlElement as HtmlElement, SelectElement as SelectElement
from scrapy.http.request import Request as Request
from scrapy.http.response.text import TextResponse as TextResponse
from scrapy.utils.python import is_listlike as is_listlike, to_bytes as to_bytes
from scrapy.utils.response import get_base_url as get_base_url

FormRequestTypeVar = TypeVar("FormRequestTypeVar", bound="FormRequest")
FormdataType = Optional[Union[dict, List[Tuple[str, str]]]]

class FormRequest(Request):
    valid_form_methods: Incomplete
    def __init__(self, *args, formdata: FormdataType = ..., **kwargs) -> None: ...
    @classmethod
    def from_response(
        cls,
        response: TextResponse,
        formname: Optional[str] = ...,
        formid: Optional[str] = ...,
        formnumber: Optional[int] = ...,
        formdata: FormdataType = ...,
        clickdata: Optional[dict] = ...,
        dont_click: bool = ...,
        formxpath: Optional[str] = ...,
        formcss: Optional[str] = ...,
        **kwargs,
    ) -> FormRequestTypeVar: ...
