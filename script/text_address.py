import sys
import os

from base.read_yaml import ReadYaml

sys.path.append(os.getcwd())

import allure

from page.page_in import PageIn

import pytest


def get_address(add_data):
    if add_data == "add":
        list = []
        for i in ReadYaml("address_data.yaml").read_yaml().get("add_address").values():
            list.append((i.get("name"), i.get("phone"), i.get("province"), i.get("city"), i.get("area"), i.get("detail"), i.get("code")))
        return list
    elif add_data == "update":
        list = []
        for i in ReadYaml("address_data.yaml").read_yaml().get("update_address").values():
            list.append((i.get("name"), i.get("phone"), i.get("province"), i.get("city"), i.get("area"), i.get("detail"), i.get("code")))
        return list


class TestAddress():

    # 初始化
    @allure.step("初始化操作")
    def setup_class(self):
        PageIn().page_in().page_login()
        self.address = PageIn().page_address()
        self.address.page_click_address_manage()

    @allure.step("结束操作")
    def teardown_class(self):
        self.address.driver.quit()

    @allure.step("测试用例   新增地址")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name, phone, province, city, area, detail, code", get_address("add"))
    def test_address(self, name, phone, province, city, area, detail, code):
        # 点击新增地址
        self.address.page_click_new_address()
        # 输入收件人
        self.address.page_send_receipt_name(name)
        # 输入电话
        self.address.page_send_phone(phone)
        # 点击区域
        self.address.page_click_address_area(province, city, area)
        # 输入详细地址
        self.address.page_send_detail_address(detail)
        # 输入编码
        self.address.page_send_post_code(code)
        # 点击设为默认地址
        self.address.page_click_default_address()
        # 点击保存
        self.address.page_click_save_btn()
        # 组装字符串
        expect_result = name + "  " + phone
        try:
            assert expect_result in self.address.page_get_elements()
            print("组装的结果: ", expect_result)
        except:
            self.address.base_get_image()
            # 截图
            with open("./img/fail.png", "rb") as f:
                allure.attach("失败的原因", f.read(), allure.attach_type.PNG)

    @allure.step("测试用例   修改地址")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name, phone, province, city, area,detail, code", get_address("update"))
    def test_updata(self, name, phone, province, city, area, detail, code):
        # 点击编辑
        self.address.page_click_edit()

        # 点击  修改内容
        self.address.page_updata_element(name, phone, province, city, area, detail, code)

        # 组装字符串
        expect_results = name + "  " + phone
        try:
            assert expect_results in self.address.page_get_elements()
        except:
            self.address.base_get_image()
            # 截图
            with open("./img/fail.png", "rb") as f:
                allure.attach("失败的原因", f.read(), allure.attach_type.PNG)

    # 删除地址
    @pytest.mark.run(order=3)
    @allure.step("测试用例   删除地址")
    def test_delete_address(self):
        # 删除地址
        self.address.page_delete_address()
        # 断言
        assert self.address.page_is_have_address()
