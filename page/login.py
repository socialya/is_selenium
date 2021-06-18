from selenium.webdriver.common.by import By

from web_xiaoan.base.basepage import BasePage


class Login(BasePage):
    def login(self):
        self.steps("../step/login_step.yml")
    def get_login_err_toast(self):
        return self.steps("../step/login_step.yml")
    def get_success_toast(self):
        return self.steps("../step/login_step.yml")
