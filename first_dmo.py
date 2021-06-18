from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class TestLogin():
    def setup_class(self):
        options = Options()
        options.add_argument('--start-maximized')
        self.driver=webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.xiaoanjujia.com/user.php")
    @pytest.mark.parametrize("number,pwd,expected_value",[("17610820178","qwe12345","用户名或密码错误"),("1761082","","请输入密码")])
    def test_login(self,number,pwd,expected_value):
        self.driver.find_element(By.ID,"username").send_keys(f"{number}")
        self.driver.find_element(By.ID,"nloginpwd").send_keys(f"{pwd}")
        ele=WebDriverWait(self.driver,10).until(Ec.visibility_of_element_located((By.ID, "loginSubmit")))
        self.driver.find_element(By.ID, "loginSubmit").click()
        sleep(3)
        err_msg=self.driver.find_element("class name","msg-error").text
        assert expected_value == err_msg
    def teardown(self):
        self.driver.refresh()
    def teardown_class(self):
        self.driver.quit()
