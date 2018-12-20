from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    # 封装find_element
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 封装find_elements
    def base_find_elements(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def base_send_keys(self, loc, value):
        el = self.base_find(loc)
        el.clear()
        el.send_keys(value)

    def base_click(self, loc):
        self.base_find(loc).click()

    def base_text(self, loc):
        return self.base_find(loc).text

    def base_get_image(self):
        self.driver.get_screenshot_as_file("./img/fail.png")

    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    def base_get_toset(self, msg):
        loc = By.XPATH, "//*[contains(@text, '%s')]" % msg
        return msg in self.base_find(loc, timeout=5, poll=0.1).text

    # 根据文本,查找元素
    def base_text_get_element(self, text):
        loc = By.XPATH, "//*[contains(@text,'%s')]" %text
        return self.base_find(loc, timeout=20, poll=0.1)
    def base_text_click(self, text):
        self.base_text_get_element(text).click()

    # 根据文本,获取一组元素
    def base_text_get_elements(self, text):
        loc = By.XPATH, "//*[contains(@text,'%s')]" % text
        return self.base_find_elements(loc, timeout=20, poll=0.1)
    def base_text_click_elements(self, text, num=0):

        self.base_text_get_elements(text)[num].click()
