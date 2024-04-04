import requests
from behave import *
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

@given('I set the GET endpoint for fetching country names')
def step_impl (context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addEndpoint
    context.headers = {"Content-Type": "application/json"}


@when('I send GET HTTP request')
def step_impl (context):
    context.response = requests.get(context.url , headers=context.headers, )

@then('I expect the HTTP response code of "GET" to be "200" and get country names')
def step_impl(context):
    #print(context.response.json())
    assert context.response.status_code == 200
    response_json = context.response.json()
    #print(context.response.json()[0])
    for response in response_json :
        getjson_response = response['name']['common']
        print("The country name is " , getjson_response)

    # for json in getjson_response :
    #     #print(json)
    #     if json in 'name' :
    #         print(json['common'])



@given('I set the GET endpoint for fetching country names which does not exist')
def step_impl (context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addNonExistingCurrency
    context.headers = {"Content-Type": "application/json"}


@when('I send a GET HTTP request')
def step_impl (context):
    context.response = requests.get(context.url , headers=context.headers, )

@then('I expect the HTTP response code of "GET" to be "404" and did not get the country names')
def step_impl(context):
    #print(context.response.json())
    assert context.response.status_code == 404
    response_json = context.response.json()
    print("Message for non existing currency" , response_json)

