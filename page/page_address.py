import page
from base.base import Base


class PageAddress(Base):

    # 点击地址管理
    def page_click_address_manage(self):
        self.base_click(page.address_manage)

    # 点击 新增地址
    def page_click_new_address(self):
        self.base_click(page.address_add_new_btn)

    # 输入 收件人
    def page_send_receipt_name(self, name):
        self.base_send_keys(page.address_receipt_name, name)

    # 输入电话
    def page_send_phone(self, phone):
        self.base_send_keys(page.address_add_phone, phone)

    # 点击区域
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
    def page_send_detail_address(self, detail):
        self.base_send_keys(page.address_detail_addr_info, detail)

    # 输入 邮编
    def page_send_post_code(self, code):
        self.base_send_keys(page.address_post_code, code)

    # 点击 设为默认地址
    def page_click_default_address(self):
        self.base_click(page.address_default)

    # 点击保存
    def page_click_save_btn(self):
        self.base_click(page.address_save)

    # 用elements找元素
    def page_get_elements(self):
        els = self.base_find_elements(page.receipt_name)
        # 行内循环
        return [i.text for i in els]



    # 点击编辑  根据传入的文本进行点击
    def page_click_edit(self, text="编辑"):
        self.base_text_click(text)
    # 点击修改,默认点击第一个修改元素
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











