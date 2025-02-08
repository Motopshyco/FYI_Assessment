from pages.submit_a_request_page import SubmitARequestPage
from behave import step
from hamcrest import *

@step(u'The user can see the submit a request page')
def verify_actual_submit_a_request_page(context):
    """
    This method verifies if the user is on the submit a request page
    :param context: object to use any parameter during the execution
    """
    context.submit_a_request_page = SubmitARequestPage(context.driver)
    page_title = context.submit_a_request_page.get_page_title()
    current_url = context.driver.current_url
    assert_that(page_title, equal_to('Submit a request'), 'the button does not redirect to the correct page')
    assert_that(current_url, contains_string('requests/new'), 'the app is not on the submit a request page')

@step(u'The user is on the submit a request page')
def open_on_submit_a_request_page(context):
    """
    This method open submit a request page in the FYI application for the user
    :param context: object to use any parameter during the execution
    """
    context.submit_a_request_page = SubmitARequestPage(context.driver)
    context.submit_a_request_page.open_submit_a_request_page()

@step(u'The user search "{text_to_search}" on the search field')
def write_on_search_field(context, text_to_search):
    """
    This method search the desired text on the search field
    :param context: object to use any parameter during the execution
    :param text_to_search: string, text to search on the app
    """
    context.submit_a_request_page.search_text(text_to_search)

@step(u'The user should received "{number_of_articles}" articles')
def verify_number_of_articles(context, number_of_articles):
    """
    This method verifies if the page is returning the number of articles expected
    :param context: object to use any parameter during the execution
    :param number_of_articles:
    """
    quantity_of_results = context.submit_a_request_page.get_quantity_results()
    assert_that(quantity_of_results, contains_string(number_of_articles), f'the search got {quantity_of_results}')