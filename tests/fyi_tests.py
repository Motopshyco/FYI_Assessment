import unittest
from selenium import webdriver

from pages.common_page import CommonPage
from pages.help_page import HelpPage
from pages.submit_a_request_page import SubmitARequestPage


class FyiTests(unittest.TestCase):

    def setUp(self):
        """
        This method open and maximize the browser before each scenario and creates the instance for each page
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://fyi.ai/')
        self.common_page = CommonPage(self.driver)
        self.help_page = HelpPage(self.driver)
        self.submit_a_request_page = SubmitARequestPage(self.driver)

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
        self.common_page.display_hamburger_menu()
        errors = self.common_page.check_hamburger_menu_options(options_list)

        if errors:
            raise AssertionError('The tests failed with this errors: \n' + '\n'.join(errors))

    def test_contact_support_button(self):
        """
        This test verifies if the contact support button redirects to the "submit request" page
        """
        self.common_page.display_hamburger_menu()
        self.common_page.click_hamburger_option('Help')
        self.common_page.change_to_a_new_page()
        self.help_page.click_contact_support_button()
        page_title = self.submit_a_request_page.get_page_title()

        self.assertEqual(page_title, 'Submit a request', 'the button does not redirect to the correct page')

    def test_search_input_results(self):
        """
        This tests verifies how many results you get after search AI
        """
        self.driver.get('https://help.fyi.me/hc/en-us/requests/new')
        self.submit_a_request_page.search_text('AI')
        quantity_of_results = self.submit_a_request_page.get_quantity_results()

        self.assertIn('15', quantity_of_results, f'the search got {quantity_of_results}')

    def tearDown(self):
        """
        This method close the browser after each scenario
        """
        self.driver.quit()