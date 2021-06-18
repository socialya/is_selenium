from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web_xiaoan.base.basepage import BasePage
from web_xiaoan.common.read_config import read_config
from web_xiaoan.page.main import Main

run=read_config()['run']
class Web(BasePage):
    def get_driver(self):
        if self._driver is None:
            if run['is_headless'] ==False:
                options = Options()
                options.add_argument('--start-maximized')
            else:
                options = Options()
                options.add_argument('--start-maximized')
                options.add_argument("--headless")
            if run['broser'] =="chrome":
                    self._driver=webdriver.Chrome(options=options)
            elif run['broser'] =="firefox":
                self._driver = webdriver.Firefox(options=options)
            elif run['broser']=="Ie":
                self._driver = webdriver.Ie(options=options)
            else:
                print("没有设置浏览器")
        self._driver.implicitly_wait(10)
        return self
    def main(self)->Main:
        return Main(self._driver)
    def refresh(self):
        self._driver.refresh()
    def close_driver(self):
        self._driver.quit()