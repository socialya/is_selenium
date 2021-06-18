from selenium.webdriver.common.by import By

from base.basepage import BasePage
from page.login import Login


class Main(BasePage):
    _base_url = "https://www.xiaoanjujia.com/index.php"
    def goto_login(self):
        self.steps(r"C:\Users\DELL\Desktop\集中\web_xiaoan\step\main_step.yml")
        return Login(self._driver)