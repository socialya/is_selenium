import inspect
import json

import yaml
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
class BasePage:

    _driver:WebDriver
    _base_url=""
    _params={}
    def __init__(self,driver:WebDriver=None):
        self._driver=driver
        if self._base_url !="":
            self._driver.get(self._base_url)
    def find(self,method,locator:str=None):
        element:WebElement
        if isinstance(method,tuple):
            element=self._driver.find_element(*method)
        else:
            element=self._driver.find_element(method,locator)
        return element
    def wait_visibility(self,method,locator,poll_frequency:float=0.5,timeout:int=10):
        element:WebElement
        try:
           element= WebDriverWait(self._driver,poll_frequency,timeout).until(Ec.visibility_of_element_located((method,locator)))
        except Exception as e:
            print("超时")
        else:
            print("查找成功")
            return element
    def wait_click(self,method,locator,poll_frequency:float=0.5,timeout:int=10):
        try:
            element=WebDriverWait(self._driver, poll_frequency, timeout).until(Ec.element_to_be_clickable((method, locator)))
        except Exception as e:
            print("超时")
        else:
            print("查找成功")
            return element

    def click(self,method,locator):
        element:WebElement
        element=self.wait_click(method,locator)
        try:
            element.click()
        except Exception as e:
            print("报错了")
        else:
            print("点击成功")
    def send_text(self,method,locator,value):
        element:WebElement
        element=self.wait_visibility(method,locator)
        try:
            element.send_keys(value)
        except Exception as e :
            print("报错")
        else:
            print("输入成功")
    def get_text(self,method,locator):
        element:WebElement
        element=self.wait_visibility(method,locator)
        try:
            ele_text=element.text
        except Exception as  e:
            print("报错了")
        else:
            print("获取文本成功")
            return ele_text

    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            fun_name=inspect.stack()[1].function
            step_datas=yaml.safe_load(f)[fun_name]
        step_str=json.dumps(step_datas)
        for k,v in self._params.items():
            step_str=step_str.replace(f"${{{k}}}",v)
        steps=json.loads(step_str)
        for step in steps:
            if "action" in step.keys():
                action=step['action']
                if "click" == action:
                    self.click(step['by'],step['locator'])
                if "send" == action:
                    self.send_text(step['by'],step['locator'],step['value'])
                if "get_text"==action:
                    return self.get_text(step['by'],step['locator'])




