from behave import given, when, then, step
from behave_http.steps import *
import requests

@given(u'I send get withdraw history request')
def step_impl(context):
    context.execute_steps('''
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a GET request to "/api/v2/withdraw/"
    Then the response status should be 200
    ''')

@then(u'I cancel the withdraw request with id')
def cancel_withdraw_by_id(context):
    url = str(context.server) + "/api/v2/withdraw/" + str(context.template_data['id']) + "/cancel/"
    context.response = requests.post(
        url, data=context.data, headers=context.headers, auth=context.auth,
        verify=context.verify_ssl)



@then(u'I cancel all the requests which "{id}" in the history list')
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




