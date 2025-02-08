from pages.common_page import CommonPage
from behave import step
from hamcrest import *

@step(u'The user is on home page')
def open_on_home_page(context):
    """
    This method open the home page in the FYI application for the user
    :param context: object to use any parameter during the execution
    """
    context.common_page = CommonPage(context.driver)
    context.common_page.open_home_page()

@step(u'The user displays the hamburger menu')
def click_hamburger_menu_button(context):
    """
    This method opens the hamburger menu in the app
    :param context: object to use any parameter during the execution
    """
    context.common_page.display_hamburger_menu()

@step(u'The user clicks the "{option}" option on the menu')
def select_option_on_the_menu(context, option):
    """
    This method click an option in the hamburger menu
    :param context: object to use any parameter during the execution
    :param option: string, desired option to click in the hamburger menu
    """
    context.common_page.click_hamburger_option(option)

@step(u'The user can see "{expected_copy}" copyright on the page footer')
def verify_copyright(context, expected_copy):
    """
    This method verifies if the copyright on the footer of the page is expected
    :param context: object to use any parameter during the execution
    :param expected_copy: string, expected copyright on the page
    """
    actual_copy = context.common_page.get_copyright_text()
    assert_that(actual_copy, equal_to(expected_copy), f'the actual copyright is: {actual_copy}')

@step(u'The user validates if the options "{expected_options}" are the displayed on the hamburger menu')
def verify_hamburger_menu_option(context, expected_options):
    """
    This method verifies if a list of options are displayed on the hamburger menu
    :param context: object to use any parameter during the execution
    :param expected_options: List, list of options to verify in the hamburger menu
    """
    expected_options = expected_options.split(', ')
    errors = context.common_page.check_hamburger_menu_options(expected_options)
    if errors:
        raise AssertionError('The tests failed with this errors: \n' + '\n'.join(errors))