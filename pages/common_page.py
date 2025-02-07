from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CommonPage(BasePage):
    #side menu locators
    _hamburger_menu_button = (By.CSS_SELECTOR, 'nav[class*="u-menu-hamburger"] div[class="menu-collapse"]')
    _hamburger_menu_option = lambda self, option: (
    By.XPATH, f'//ul[contains(@class, "u-text-hover-custom-color-1")] //a[contains(text(), "{option}")]')

    #footer locators
    _copyright_text_ = (By.CSS_SELECTOR, 'footer p[class*="u-text-1"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://fyi.ai/')

    def display_hamburger_menu(self):
        """
        This method displays the menu from the hamburger button
        """
        self.click_element(self._hamburger_menu_button)

    def click_hamburger_option(self, menu_option):
        """
        This method clicks the desired option in the menu displayed by the hamburger button
        :param menu_option: string, option to click in the menu
        """
        self.click_element(self._hamburger_menu_option(menu_option))

    def get_copyright_text(self):
        """
        this method get the copyright text at the footer of the page
        :return: string, copyright text
        """
        return self.wait_element_to_visible(self._copyright_text_).text