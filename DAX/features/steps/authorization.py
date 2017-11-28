from behave import given, when, then, step
from behave_http.steps import *
import base64
import requests
#
@given(u'I am Logged in')
def step_impl(context):
    context.execute_steps('''
        Given I set  "authorization" in header
        Given I am using server "$SERVER"
        When I make a POST request to "/api.php/account/authenticate/"
        Then I create the jwt and store it in "jwt"
    ''')

@given(u'I am logged dax')
def step_impl(context):
    context.execute_steps('''
        Given  I am Logged in
        Given I am using server "$DAX"
        When I send a  POST request to "/login/"
        Then the response status should be 200
        And the response body should contain "key"
        And the response body should contain "msg"
        When I store the JSON at path "key" in "key"
        And I store the JSON at path "user_info.username" in "username"
        Then I create the AccessToken and store it in "token"
        And I set "Authorization" header to "token"

    ''')


@given('I set  "authorization" in header')
def set_auth(context):
    user_pass_string = context.username+ ":" + context.password
    hash_string = base64.b64encode(user_pass_string.encode('ascii'))
    ## convert byte to str
    decode_hash_str = str(hash_string,'utf-8')
    Basic_hash_string = "Basic" +" "+decode_hash_str
    context.headers  = {
        'authorization' : Basic_hash_string ,
    }

@then(u'I create the jwt and store it in "{jwt}"')
def store_for_template(context,jwt):
    context.template_data[jwt] = context.response.headers["json-web-token"]


@then(u'I create the AccessToken and store it in "{variable}"')
def store_for_template(context, variable):
    key = context.template_data["key"]
    username = context.template_data["username"]
    access_token = "ApiKey %s:%s" % (username, key)
    context.template_data[variable] = access_token

#