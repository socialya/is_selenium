from time import sleep

import pytest

from test_cases.basecase import BaseCase


class Test_login(BaseCase):
    def setup_class(self):
        super(Test_login, self).setup_class(self)
        self.main=self.web.main()
        self.login=self.main.goto_login()
    @pytest.mark.parametrize("username,pwd,expected",[
        ("1231223123","","请输入密码"),
        ("1231323221","asdadsad","用户名或密码错误")
    ])
    def test_err_login(self,username,pwd,expected):
        self.login._params['username']=username
        self.login._params['pwd']=pwd
        self.login.login()
        sleep(3)
        err_msg=self.login.get_login_err_toast()

        print(err_msg)
        assert expected ==err_msg
    def test_success_login(self):
        self.login._params['username']="13581813106"
        self.login._params['pwd']="zhulin666"
        self.login.login()
        sucess_name=self.login.get_success_toast()
        assert "64796685-431233" ==sucess_name

    def teardown(self):
        self.web.refresh()
if __name__ == '__main__':
    pytest.main()