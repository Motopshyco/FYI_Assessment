from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator, timeout=10):
        """
        This method gets a webElement from the locator and waits until appears in the DOM
        :param locator: tuple, locator to find a web element in the DOM
        :param timeout: number, maximum time in seconds to wait the element appears in the DOM
        :return: web element needed
        """
        selector = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        return selector

    def wait_element_to_visible(self, locator, timeout=10):
        """
        This method gets a webElement from the locator and waits until it's visible in the page
        :param locator: tuple, locator to find a web element
        :param timeout: number, maximum time in seconds to wait the element appears in the page
        :return: web element needed
        """
        selector = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        return selector

    def click_element(self, locator, timeout=10):
        """
        This method clicks a web element in the page
        :param locator: tuple, locator to find the element to click
        :param timeout: number, maximum time in seconds to wait the element appears
        """
        element = self.wait_element_to_visible(locator, timeout)
        element.click()

    def send_text_to_element(self, locator, text, timeout=10):
        """
        This method writes a specific text in the desired place at the app
        :param locator: tuple, locator to find the element to write
        :param text: string, text to send to the web element
        :param timeout: number, maximum time in seconds to wait the element appears
        """
        element = self.wait_element_to_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    def send_key_to_element(self, locator, key, timeout=10):
        """
        This method writes a specific text in the desired place at the app
        :param locator: tuple, locator to find the element to use an action
        :param key: string, key to send to the web element
        :param timeout: number, maximum time in seconds to wait the element appears
        """
        element = self.wait_element_to_visible(locator, timeout)
        element.send_keys(key)

    def get_text_from_element(self, locator, timeout = 10):
        """
        This method gets the text from a specified locator
        :param locator: tuple, locator to get the needed text
        :param timeout: number, maximum time in seconds to wait the element appears
        :return: string, text of the desired element
        """
        return self.wait_element(locator, timeout).text

    def change_to_a_new_page(self):
        """
        This method change the control to the new window, and close the previous one
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        self.driver.close()
        self.driver.switch_to.window(handles[1])
