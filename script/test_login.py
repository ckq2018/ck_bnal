import os
import sys

from base.read_txt import ReadTxt

sys.path.append(os.getcwd())

from page.page_in import PageIn
import pytest


def get_function():

    return   [("18665189551", "123456", "chenkaiqing")]


class TestLogin():

    def setup_class(self):
        self.login = PageIn().page_in()

    def teardown_class(self):
        self.login.driver.quit()

    # 参数化
    @pytest.mark.parametrize("usersname, pwd, expect_result", get_function())
    def test_login(self, usersname, pwd, expect_result):
        # 点击 我
        self.login.page_click_my()
        # 点击已有账号
        self.login.page_click_logins()
        # 输入用户名
        self.login.page_send_name(usersname)
        # 输入密码
        self.login.page_send_pwd(pwd)
        # 点击登录
        self.login.page_click_login()

        # 将获取昵称和断言一起
        # 获取昵称并捕获异常
        # try:
        #     assert expect_result in self.login.page_get_nick()
        #     点击设置和点击退出可以放在捕获异常里面,但建议放在外面
        #     self.login.page_click_set()
        #     self.login.page_exits()
        # except:
        #     pass

        # 将获取昵称和断言分开
        # 获取昵称
        self.login.page_get_nick()
        # # 断言
        try:
            assert expect_result
        except:
            #截图
            self.login.base_get_image()
            raise

        # 点击设置
        self.login.page_click_set()
        # 点击退出
        self.login.page_exits()
