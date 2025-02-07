from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HelpPage(BasePage):
    #main content locators
    _contact_support_button_ = (By.CSS_SELECTOR, 'button[title="Contact Support"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_contact_support_button(self):
        """
        This method clicks the contact support button
        """
        self.click_element(self._contact_support_button_)