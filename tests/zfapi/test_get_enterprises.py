import requests
import pytest
import os
from pytest_bdd import scenarios, given, when, then, parsers
from dotenv import load_dotenv

scenarios('../../features/zfapi/get_enterprises.feature')


load_dotenv(override=True)

# Environment variables setup based on .env file
API_URL = os.getenv('zfAPIBaseURL')
ZFAPI_TOKEN = os.getenv('zfAPIToken')

headers = {
    'Authorization': f'Token {ZFAPI_TOKEN}',
    'Content-Type':'application/json; charset=UTF-8'
}

@pytest.fixture
def api_response():
    return {}

@given('the ZF API is available')
def api_is_available():
    pass

@when(parsers.parse('the user retrieves all the enterprises from "{path}"'))
def send_get_all_enterprises(api_response,path):
    endpoint = f"{API_URL}/{path}"
    response = requests.get(endpoint, headers=headers)
    print (endpoint)
    api_response['response'] = response

@when(parsers.parse('the user retrieves the enterprise "{enterprise_id}" from "{path}"'))
def send_get_specific_enterprise(api_response,enterprise_id,path):
    endpoint = f"{API_URL}/{path}/{enterprise_id}"
    response = requests.get(endpoint, headers=headers)
    api_response['response'] = response

@when(parsers.parse('the user retrieves the protected accounts of the enterprise "{enterprise_id}" from "{path}"'))
def send_get_enterprise_protected_accounts(api_response,enterprise_id,path):
    endpoint = f"{API_URL}/{path}/{enterprise_id}/accounts"
    response = requests.get(endpoint,headers=headers)
    api_response['response'] = response

@then(parsers.parse('the status code should be "{status_code}"'))
def validate_status_code(api_response, status_code):
    response = api_response['response']
    assert response.status_code == int(status_code), f"Expected {status_code} but got {response.status_code}."

@then('the response should contain a list of enterprises')
def validate_enterprises_in_response(api_response):
    response = api_response['response']
    json_data = response.json()
    assert 'enterprises' in json_data, "Response does not contain 'enterprises'."
    assert isinstance(json_data['enterprises'], list),"'enterprises' should be a list."
    assert len(json_data['enterprises']) > 0, "Expected non-empty list of enterprises."
    for enterprise in json_data['enterprises']:
        assert 'id' in enterprise, "Each enterprise should have an id."
        assert isinstance(enterprise['id'], int), "'id' should be an integer."
        assert 'labels' in enterprise, "Each enterprise should have 'labels'."
        assert isinstance(enterprise['labels'], list), "'labels' should be a list."
        assert 'name' in enterprise, "Each enterprise should have 'name'."
        assert isinstance(enterprise['name'],str), "'name' should be a string."
        assert 'status' in enterprise, "Each enterprise should have 'status'."
        assert isinstance(enterprise['status'],list), "'status' should be a list"

@then('the response should have the protected accounts associated with the enterprise')
def validate_protected_accounts(api_response):
    response = api_response['response']
    json_data = response.json()
    assert 'entity_accounts' in json_data, "Response does not contain 'entity_accounts"
    assert isinstance(json_data['entity_accounts'], list),"'entity_accounts should be a list'."
    assert len(json_data['entity_accounts']) > 0, "Expected non-empty list of 'entity_accounts'."
    for entity_account in json_data['entity_accounts']:
        assert 'id' in entity_account, "Each entity account should have 'id'"
        assert isinstance(entity_account['id'], int), "'id' should be an integer."
        assert 'network' in entity_account, "Each entity account should have 'network'"
        assert isinstance(entity_account['network'], str), "'network' should be a string."
        assert 'account_number' in entity_account, "Each entity account should have 'account_number'"
        assert isinstance(entity_account['account_number'], str), "'account_number' should be a string."
        assert 'account_url' in entity_account, "Each entity account should have 'account_url'"
        assert isinstance(entity_account['account_url'], str), "'account_url' should be a string."
        assert 'username' in entity_account, "Each entity account should have 'username'"
        assert isinstance(entity_account['username'], str), "'username' should be a string."
        assert 'profile_image' in entity_account, "Each entity account should have 'profile_image'"
        assert isinstance(entity_account['profile_image'], str), "'profile_image' should be a string."
        assert 'display_name' in entity_account, "Each entity account should have 'display_name'"
        assert isinstance(entity_account['display_name'], str), "'display_name' should be a string."
        assert 'background_image_url' in entity_account, "Each entity account should have 'background_image_url'"
        assert isinstance(entity_account['background_image_url'], str), "'background_image_url' should be a string."
        assert 'authenticated' in entity_account, "Each entity account should have 'authenticated'"
        assert isinstance(entity_account['authenticated'], bool), "'authenticated' should be a boolean."
        assert 'locked' in entity_account, "Each entity account should have 'locked'"
        assert isinstance(entity_account['locked'], bool), "'locked' should be a boolean."
        assert 'type' in entity_account, "Each entity account should have 'type'"
        assert isinstance(entity_account['type'], str), "'type' should be a string."
        assert 'entity_id' in entity_account, "Each entity account should have 'entity_id'"
        assert isinstance(entity_account['entity_id'], int), "'entity_id' should be an integer."


