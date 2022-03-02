import configparser
import copy
import pytest

from catocli.catoclient import CATOClient

#####################################################################################
# Setup
#####################################################################################

TEST_CONFIG_PATH = '/tmp/catoclient.ini'

CATO_DEFAULT_CONFIGURATION = """[server]
url = https://192.168.1.0
apipath = /api/v0
verify_ssl = false

[general]
wait = 0

[history]
last_oppfor = 0

[auth]
catouser=fileUser
catopass=filePassword
sshuser=fileSshUser
sshpass=fileSshPassword"""

CATO_DEFAULT_CONFIGURATION_JSON_FORMAT = {
    'url': 'https://192.168.1.1',
    'apipath': '/api/v1',
    'should_verify_ssl': True,
    'wait': 1,
    'customer_id': 1,
    'cato_username': 'jsonUser',
    'cato_password': 'jsonPassword',
    'sshuser': 'jsonSshUser',
    'sshpassword': 'jsonSshPassword'
}

CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT = {
    'url': 'https://192.168.1.2',
    'apipath': '/api/v2',
    'should_verify_ssl': False,
    'wait': 2,
    'oppfor': 2,
    'catouser': 'argumentsUser',
    'catopass': 'argumentsPassword',
    'sshuser': 'argumentsSshUser',
    'sshpassword': 'argumentsSshPassword'
}

CATO_DEFAULT_CONFIGURATION_KEYWORDS_FORMAT = {
    'url': 'https://192.168.1.3',
    'apipath': '/api/v3',
    'verifyssl': True,
    'wait': 3,
    'oppfor': 3,
    'username': 'keywordsUser',
    'password': 'keywordsPassword',
    'sshuser': 'keywordsSshUser',
    'sshpassword': 'keywordsSshPassword'
}

#####################################################################################
# Utilities
#####################################################################################

def generate_default_config():
    config = configparser.ConfigParser()
    config.read_string(CATO_DEFAULT_CONFIGURATION)
    return config

#####################################################################################
# Test Cases
#####################################################################################

def test_can_create_client_blank():
    client = CATOClient()
    assert type(client) == CATOClient

def test_create_client_with_config_file():
    client = CATOClient(properties=generate_default_config())

    assert client.cato_url == 'https://192.168.1.0/api/v0/'
    assert client.base_cato_url == 'https://192.168.1.0/'
    assert client.apipath == 'api/v0'
    assert client.cato_auth_url == 'https://192.168.1.0/auth/login/'

def test_create_client_argument_priority_config_vs_arguments(create_cli_arguments):
    testArgs = create_cli_arguments()

    for attr in CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT:
        setattr(testArgs, attr, CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT[attr])

    client = CATOClient(properties=generate_default_config(),arguments=testArgs)

    assert client.cato_url == 'https://192.168.1.2/api/v2/'
    assert client.base_cato_url == 'https://192.168.1.2/'
    assert client.apipath == 'api/v2'
    assert client.cato_auth_url == 'https://192.168.1.2/auth/login/'

def test_create_client_argument_priority_arguments_vs_keywords(create_cli_arguments):
    testArgs = create_cli_arguments()

    for attr in CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT:
        setattr(testArgs, attr, CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT[attr])

    testKeywords = copy.deepcopy(CATO_DEFAULT_CONFIGURATION_KEYWORDS_FORMAT)
    testKeywords['arguments'] = testArgs

    client = CATOClient(**testKeywords)

    assert client.cato_url == 'https://192.168.1.3/api/v3/'
    assert client.base_cato_url == 'https://192.168.1.3/'
    assert client.apipath == 'api/v3'
    assert client.cato_auth_url == 'https://192.168.1.3/auth/login/'

def test_create_client_argument_priority_all_forms(create_cli_arguments):
    testArgs = create_cli_arguments()

    for attr in CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT:
        setattr(testArgs, attr, CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT[attr])

    testKeywords = copy.deepcopy(CATO_DEFAULT_CONFIGURATION_KEYWORDS_FORMAT)
    testKeywords['arguments'] = testArgs
    testKeywords['properties'] = generate_default_config()

    client = CATOClient(**testKeywords)

    assert client.cato_url == 'https://192.168.1.3/api/v3/'
    assert client.base_cato_url == 'https://192.168.1.3/'
    assert client.apipath == 'api/v3'
    assert client.cato_auth_url == 'https://192.168.1.3/auth/login/'