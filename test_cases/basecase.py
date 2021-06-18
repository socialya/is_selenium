from common.web import Web


class BaseCase():
    def setup_class(self):
        print("哈哈哈哈")
        self.web=Web().get_driver()
    def teardown_class(self):
        self.web.close_driver()