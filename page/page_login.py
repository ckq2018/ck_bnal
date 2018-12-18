import page
from base.base import Base
import allure

class PageLogin(Base):
    # 点击 我
    @allure.step("点击 我")
    def page_click_my(self):
        self.base_click(page.loc_my)

    # 点击已有账号,去登录
    @allure.step("点击 已有帐号,去登录")
    def page_click_logins(self):
        self.base_click(page.loc_logins)

    # 输入用户名
    @allure.step("输入用户名")
    def page_send_name(self, usersname):
        self.base_send_keys(page.loc_username, usersname)

    # 输入密码
    @allure.step("输入密码")
    def page_send_pwd(self, pwd):
        self.base_send_keys(page.loc_password, pwd)

    # 点击登录
    @allure.step("点击登录")
    def page_click_login(self):
        self.base_click(page.loc_login)

    # 获取昵称
    @allure.step("获取昵称")
    def page_get_nick(self):
        return self.base_text(page.loc_login_nick)

    # 点击设置
    @allure.step("点击设置")
    def page_click_set(self):
        self.base_click(page.loc_click_set)

    # 将短信提醒拖拽到修改密码
    @allure.step("将 短信提醒 拖拽到 修改密码")
    def page_drag_and_drop(self):
        el1 = self.base_find(page.loc_sms)
        el2 = self.base_find(page.loc_update_pwd)
        self.base_drag_and_drop(el1, el2)

    # 点击退出
    @allure.step("点击退出")
    def page_click_exit(self):
        self.base_click(page.loc_exit)

    # 点击确认退出
    @allure.step("点击 确认退出")
    def page_click_is_exit(self):
        self.base_click(page.loc_is_exit)

    def page_exits(self):
        self.page_drag_and_drop()
        self.page_click_exit()
        self.page_click_is_exit()






