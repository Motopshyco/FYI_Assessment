import re
import os
import allure
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

def after_step(context, step):
    """
    This method take a screenshot of each step that fails in the execution
    :param context: object to use any parameter during the execution
    :param step: each step executed in the scenario
    """
    if step.status == "failed":
        good_name = re.sub(r'[<>:"/\\|?*]', '_', step.name)
        screenshot_path = f"reports/screenshots/{good_name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        context.driver.save_screenshot(screenshot_path)

        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=step.name, attachment_type=allure.attachment_type.PNG)


def after_scenario(context, scenario):
    """
    This method close the browser after each scenario
    :param context: object to use any parameter during the execution
    :param scenario: scenario executed each time
    """
    context.driver.quit()