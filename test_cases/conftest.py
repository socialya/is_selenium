import pytest

from web_xiaoan.base.basepage import BasePage
from web_xiaoan.common.web import Web


@pytest.fixture(scope="class")
def use_driver():
    web = Web().get_driver()
    web.main()
    yield
    print("后面刷新")
    Web().get_driver().refresh()

