from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SubmitARequestPage(BasePage):
    #main content locators
    _page_title_ = (By.CSS_SELECTOR, 'div[class="container"] h1')

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text_from_element(self._page_title_)