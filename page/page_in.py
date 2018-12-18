from base.get_driver import get_driver
from page.page_login import PageLogin

driver = get_driver()

class PageIn():

    def page_in(self):
        return PageLogin(driver)
