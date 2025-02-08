from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    """
    This method opens the browser before each scenario and enable the automation.
    :param context: object to use any parameter during the execution
    :param scenario: scenario to execute each time
    """
    options = Options()
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    context.driver = Chrome(options=options)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    """
    This method close the browser after each scenario
    :param context: object to use any parameter during the execution
    :param scenario: scenario executed each time
    """
    context.driver.quit()