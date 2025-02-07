from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class SubmitARequestPage(BasePage):
    #main content locators
    _page_title_ = (By.CSS_SELECTOR, 'div[class="container"] h1')
    _search_input_ = (By.ID, 'query')
    _quantity_of_results_after_search_ = (By.CSS_SELECTOR, 'h1[class="search-results-subheading"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text_from_element(self._page_title_)

    def search_text(self, text):
        self.send_text_to_element(self._search_input_, text)
        self.send_key_to_element(self._search_input_, Keys.ENTER)

    def get_quantity_results(self):
        return self.get_text_from_element(self._quantity_of_results_after_search_)