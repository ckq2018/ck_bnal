import os
import sys

import allure

sys.path.append(os.getcwd())

import pytest
from base.read_txt import ReadTxt
from base.read_yaml import ReadYaml
from page.page_in import PageIn



def get_function():
    list = []
    for data in ReadYaml("login_data.yaml").read_yaml().values():
        list.append((data.get("usersname"), data.get("pwd"), data.get("expect_result"), data.get("expect_toast")))
    return list


class TestLogin():

    def setup_class(self):
        self.login = PageIn().page_in()
        # 点击 我
        self.login.page_click_my()
        # 点击已有账号
        self.login.page_click_logins()

    def teardown_class(self):
        self.login.driver.quit()

    # 参数化
    @pytest.mark.parametrize("usersname, p"
                             "wd, expect_result, expect_toast", get_function())
    @allure.step("美妙的测试之旅即将开始")
    def test_login(self, usersname, pwd, expect_result, expect_toast):
        if expect_result:
            try:
                # 输入用户名
                self.login.page_send_name(usersname)
                # 输入密码
                self.login.page_send_pwd(pwd)
                # 点击登录
                self.login.page_click_login()
                assert expect_result in self.login.page_get_nick()
                # 点击设置
                self.login.page_click_set()
                # 点击退出
                self.login.page_exits()
                # 点击 我
                self.login.page_click_my()
                # 点击已有账号
                self.login.page_click_logins()
            except AssertionError:
                self.login.base_get_image()
                with open("./img/fail.png", "rb") as f:
                    allure.attach("失败原因", f.read(), allure.attach_type.PNG)
        else :
            try:
                # 输入用户名
                self.login.page_send_name(usersname)
                # 输入密码
                self.login.page_send_pwd(pwd)
                # 点击登录
                self.login.page_click_login()
                # assert expect_toast in self.login.base_get_toset()
                assert expect_toast in self.login.base_get_toset()
            except AssertionError:
                self.login.base_get_image()
                with open("./img/fail.png", "rb") as f:
                    allure.attach("失败原因", f.read(), allure.attach_type.PNG)
