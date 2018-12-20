import sys
import os

sys.path.append(os.getcwd())

import allure

from page.page_in import PageIn

import pytest


def get_address():

    return [("王五", "13838387777", "广东", "东莞", "", "人民路55号", "100086")]

def get_data1():

    return [("王小五", "13838388888", "浙江", "杭州", "上城", "解放路88号", "100010")]

class TestAddress():

    def setup_class(self):
        PageIn().page_in().page_login()
        self.address = PageIn().page_address()
        self.address.page_click_address_manage()

    def teardown_class(self):
        self.address.driver.quit()

    @pytest.mark.parametrize("name, phone, province, city, area, detail, code", get_address())
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

    @pytest.mark.parametrize("name, phone, province, city, area,detail, code", get_data1())
    def test_updata(self, name, phone, province, city, area,detail, code):
        #点击编辑
        self.address.page_click_edit()

        #点击  修改内容
        self.address.page_updata_element(name, phone, province, city, area,detail, code)

        # 组装字符串
        expect_results = name + "  " + phone
        try:
            assert expect_results in self.address.page_get_elements()
            print("组装的结果: ", expect_results)
        except:
            self.address.base_get_image()
            # 截图
            with open("./img/fail.png", "rb") as f:
                allure.attach("失败的原因", f.read(), allure.attach_type.PNG)