from behave_http.environment import before_scenario

def before_all(context):
    context.username = 'jia12@yopmail.com'
    context.password = 'Test1234'


