from _typeshed import Incomplete

from twisted.web import util

class SiteTest:
    site: Incomplete
    baseurl: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def url(self, path): ...

class NoMetaRefreshRedirect(util.Redirect):
    def render(self, request): ...

def test_site(): ...
