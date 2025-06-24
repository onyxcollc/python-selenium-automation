from behave import given, when, then



@given('Open sign in page')
def open_signin_page(context):
    context.app.signin_page.open_signin_page()

@when('Click Terms and Conditions link')
def click_terms_and_conditions_link(context):
    context.app.signin_page.click_terms_and_conditions()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_conditions_page.verify_tc_opened()
