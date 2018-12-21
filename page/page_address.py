import allure

import page
from base.base import Base

class PageAddress(Base):

    # 点击地址管理
    @allure.step("点击 地址管理")
    def page_click_address_manage(self):
        self.base_click(page.address_manage)

    # 点击 新增地址
    @allure.step("点击 新增地址")
    def page_click_new_address(self):
        self.base_click(page.address_add_new_btn)

    # 输入 收件人
    @allure.step("输入 收件人")
    def page_send_receipt_name(self, name):
        self.base_send_keys(page.address_receipt_name, name)

    # 输入电话
    @allure.step("输入 电话")
    def page_send_phone(self, phone):
        self.base_send_keys(page.address_add_phone, phone)

    # 点击区域
    @allure.step("点击 区域")
    def page_click_address_area(self, province, city, area):
        # 点击区域
        self.base_click(page.address_area)
        # 点击 省   (先忽略直辖市)
        self.base_text_click(province)
        # 点击市
        self.base_text_click(city)
        # 点击区
        self.base_text_click(area)

    # 输入 详细地址
    @allure.step("输入 详细地址")
    def page_send_detail_address(self, detail):
        self.base_send_keys(page.address_detail_addr_info, detail)

    # 输入 邮编
    @allure.step("输入 邮编")
    def page_send_post_code(self, code):
        self.base_send_keys(page.address_post_code, code)

    # 点击 设为默认地址
    @allure.step("点击  设为默认地址")
    def page_click_default_address(self):
        self.base_click(page.address_default)

    # 点击保存
    @allure.step("点击 保存")
    def page_click_save_btn(self):
        self.base_click(page.address_save)

    # 用elements找元素 , 获取地址列表的个数
    @allure.step("获取地址列表的个数")
    def page_get_elements(self):
        els = self.base_find_elements(page.receipt_name)
        # 行内循环
        return [i.text for i in els]

    # 点击编辑  根据传入的文本进行点击
    @allure.step("点击  编辑")
    def page_click_edit(self, text="编辑"):
        self.base_text_click(text)

    # 点击修改,默认点击第一个修改元素
    @allure.step("点击 修改")
    def page_updata_element(self, name, phone, province, city, area, detail, code):
        # 点击修改吧 根据传入的文本获取的一组元素,进行点击(默认第一个)
        self.base_text_click_elements("修改")
        # 输入收件人
        self.page_send_receipt_name(name)
        # 输入电话
        self.page_send_phone(phone)
        # 点击区域
        self.page_click_address_area(province, city, area)
        # 输入详细地址
        self.page_send_detail_address(detail)
        # 输入邮编
        self.page_send_post_code(code)
        # 单击保存
        self.page_click_save_btn()

    # 删除时点击  是否确认
    @allure.step("点击 删除确认")
    def page_click_is_ok(self):
        self.base_click(page.address_is_ok)

    # 删除地址
    @allure.step("点击  地址")
    def page_delete_address(self):
    # 循环地址个数
        for data in range(len(self.page_get_elements())):
            # 点击编辑
            self.page_click_edit()
            # 获取编辑的所有元素,并点击第一个
            self.base_text_click_elements("删除")
            # 点击确认
            self.page_click_is_ok()

    # 断言    判断是否有地址
    @allure.step("断言 是否还有地址")
    def page_is_have_address(self):
        try:
            self.base_find_elements(page.receipt_name, timeout=3)
            allure.attach("未删除干净", "")
            return False
        except:
            allure.attach("删除干净", "")
            return True
