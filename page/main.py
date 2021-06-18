from selenium.webdriver.common.by import By

from web_xiaoan.base.basepage import BasePage
from web_xiaoan.page.login import Login


class Main(BasePage):
    _base_url = "https://www.xiaoanjujia.com/index.php"
    def goto_login(self):
        self.steps("../step/main_step.yml")
        return Login(self._driver)