from pages.help_page import HelpPage
from behave import step

@step(u'The user click the contact support button on the help page')
def go_to_contact_support_page(context):
    """
    This method click the contact support button on the help page
    :param context: object to use any parameter during the execution
    """
    context.help_page = HelpPage(context.driver)
    context.help_page.change_to_a_new_page()
    context.help_page.click_contact_support_button()