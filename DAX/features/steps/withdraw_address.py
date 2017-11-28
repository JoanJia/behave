from behave import given, when, then, step
from behave_http.steps import *
import base64
import requests


@when(u'I create a withdraw address')
def create_withdraw_address(context):
    context.execute_steps(
    '''
    When I make a POST request to "/api/v2/withdraw_address/"
    """
    {
        "coin_type": "BTC",
        "address": "mmA4ND54mYy73G3eAifHLNxB2z4YKeDu2J"
    }
    """
    Then the response status should be 200
    And the response body should contain "results"
    '''
    )

@when(u'get withdraw history')
def get_withdraw_history(context):
    context.execute_steps(
        '''
            Scenario:  get btc withdraw address
                Given I am logged dax
                And I set "Content-Type" header to "application/json"
                When I make a GET request to "/api/v2/withdraw_address/?coin_type=BTC"
                Then the response status should be 200
                And the response body should contain "results"

        '''
    )

@then(u'delete all the address which "{id}" in the history list')
@dereference_step_parameters_and_data
def store_for_template(context, id):
    results = jpath.get("results", context.response.json())
    count = jpath.get("count", context.response.json())
    if count != 0 :
        for result in results:
            if result['status'] != 'CANCELED':
                context.template_data[id] = result['id']
                url = str(context.server)+ "/api/v2/withdraw/"+str(context.template_data[id])+"/cancel/"
                context.response = requests.post(
        url, data=context.data, headers=context.headers, auth=context.auth,
        verify=context.verify_ssl)
                ensure(context.response.status_code).equals(200)




