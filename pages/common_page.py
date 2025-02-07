from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common import TimeoutException

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

    def get_hamburger_option(self, menu_option):
        """
        This method gets the desired element for the hamburger menu
        :param menu_option: string, desired option in the hamburger menu
        :return: web element, desired web element in the hamburger menu
        """
        return self.wait_element(self._hamburger_menu_option(menu_option))

    def click_hamburger_option(self, menu_option):
        """
        This method clicks the desired option in the menu displayed by the hamburger button
        :param menu_option: string, option to click in the menu
        """
        self.click_element(self._hamburger_menu_option(menu_option))

    def get_copyright_text(self):
        """
        This method get the copyright text at the footer of the page
        :return: string, copyright text
        """
        return self.get_text_from_element(self._copyright_text_)

    def check_hamburger_menu_options(self, options_list):
        """
        This method check if the menu displayed by the hamburger has all the desired options for the user
        :param options_list: list, options desired in the menu
        :return: list, errors if any option is not on the menu
        """
        errors = []
        self.display_hamburger_menu()
        for option in options_list:
            try:
                self.get_hamburger_option(option)
                print(f'✅ the element {option} is on the menu')
            except TimeoutException:
                error = f'❌ Test Failed: the element {option} is not on the menu'
                errors.append(error)
        return errors