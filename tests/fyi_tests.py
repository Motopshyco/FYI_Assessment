import unittest
from selenium import webdriver


from pages.common_page import CommonPage

class FyiTests(unittest.TestCase):

    def setUp(self):
        """
        This method open and maximize the browser before each scenario
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.common_page = CommonPage(self.driver)

    def test_terms_of_service_copyright(self):
        """
        This test validates if the copyright in the terms of service page is correct
        """
        self.common_page.display_hamburger_menu()
        self.common_page.click_hamburger_option('Terms of Service')
        actual_copy = self.common_page.get_copyright_text()

        self.assertEqual(actual_copy, '©2024 FYI.FYI, Inc.', f'the actual copyright is: {actual_copy}')

    def test_hamburger_menu_option(self):
        """
        This test validates if the hamburger menu contains the correct user selection options
        """
        options_list = ["Home", "Help", "About Us", "The Team", "Press", "Terms of Service", "Privacy Policy"]
        errors = self.common_page.check_hamburger_menu_options(options_list)

        if errors:
            raise AssertionError('The tests failed with this errors: \n' + '\n'.join(errors))

    def tearDown(self):
        """
        This method close the browser after each scenario
        """
        self.driver.quit()