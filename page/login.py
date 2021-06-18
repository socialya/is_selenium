from selenium.webdriver.common.by import By

from base.basepage import BasePage


class Login(BasePage):
    def login(self):
        self.steps(r"C:\Users\DELL\Desktop\集中\web_xiaoan\step\login_step.yml")
    def get_login_err_toast(self):
        return self.steps(r"C:\Users\DELL\Desktop\集中\web_xiaoan\step\login_step.yml")
    def get_success_toast(self):
        return self.steps(r"C:\Users\DELL\Desktop\集中\web_xiaoan\step\login_step.yml")
