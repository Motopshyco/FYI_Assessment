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

    def open_submit_a_request_page(self):
        """
        This method open submit a request page on the FYI web application
        """
        self.driver.get('https://help.fyi.me/hc/en-us/requests/new')

    def get_page_title(self):
        """
        This method gets the title of the submit a request page
        """
        return self.get_text_from_element(self._page_title_)

    def search_text(self, text):
        """
        This method search a specified text on the application
        :param text: string, text to search on the application
        """
        self.send_text_to_element(self._search_input_, text)
        self.send_key_to_element(self._search_input_, Keys.ENTER)

    def get_quantity_results(self):
        """
        This method gets the number of articles returned by the page
        :return: string, number of articles returned by the page
        """
        return self.get_text_from_element(self._quantity_of_results_after_search_)