import unittest
from selenium import webdriver
from pages.common_page import CommonPage

class FyiTests(unittest.TestCase):

    def setUp(self):
        """
        this method open and maximize the browser before each scenario
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.common_page = CommonPage(self.driver)

    def test_terms_of_service_copyright(self):
        """
        this test validate if the copyright in the terms of service page is correct
        """
        self.common_page.display_hamburger_menu()
        self.common_page.click_hamburger_option('Terms of Service')
        actual_copy = self.common_page.get_copyright_text()

        self.assertEqual(actual_copy, '©2024 FYI.FYI, Inc.', f'the actual copyright is: {actual_copy}')

    def tearDown(self):
        """
        this method close the browser after each scenario
        """
        self.driver.quit()