from behave import given, when, then, step
from behave_http.steps import *
import requests


@behave.then('I set "{var}" header to "{value}"')
def step_impl(context, var, value):
    context.headers = {}
    context.headers[var.encode('ascii')] = context.template_data[value]


@when('I send a  POST request to "{url_path_segment}"')
def send_request(context,url_path_segment):
    login_url = append_path(context.server, url_path_segment)
    context.data = {
        'email': context.username,
        'oauth_token': context.template_data["jwt"],
        'oauth_provider': 'btcc'
    }
    context.response = requests.request("POST",url=login_url,data = context.data)

@behave.then('the response body should contain one of "{contents}"')
@dereference_step_parameters_and_data
def response_status_in(context, contents):
    ensure(context.response.content.decode('utf-8')).contains_one_of(contents.split(','))

