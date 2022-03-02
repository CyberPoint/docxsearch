import configparser
import copy
import json
import pytest

from catocli.catoclient import CATOClient
import scripts.catocli as catocli

#####################################################################################
# Setup
#####################################################################################

default_config_path = "%s/%s" % (catocli.get_user_catodir(), catocli.CATO_CONFIGURATION_FILE)

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
    'cato_username': 'jsonUser',
    'cato_password': 'jsonPassword',
    'sshuser': 'jsonSshUser',
    'sshpassword': 'jsonSshPassword'
}

CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT = {
}

CATO_DEFAULT_CONFIGURATION_KEYWORDS_FORMAT = {
}

TARGETS = [
    {
        "id": 406,
        "value": "192.168.1.1",
        "type": "ipaddress",
        "customer": 5
    },
    {
        "id": 407,
        "value": "192.168.1.2",
        "type": "ipaddress",
        "customer": 5
    },
    {
        "id": 408,
        "value": "192.168.1.100",
        "type": "ipaddress",
        "customer": 5
    },
    {
        "id": 409,
        "value": "192.168.1.72",
        "type": "ipaddress",
        "customer": 5
    },
    {
        "id": 410,
        "value": "192.168.1.20",
        "type": "ipaddress",
        "customer": 5
    },
    {
        "id": 411,
        "value": "192.168.1.99",
        "type": "ipaddress",
        "customer": 5
    },
    {
        "id": 412,
        "value": "192.168.1.80",
        "type": "ipaddress",
        "customer": 5
    },
    {
        "id": 413,
        "value": "192.168.1.3",
        "type": "ipaddress",
        "customer": 5
    },
    {
        "id": 414,
        "value": "10.0.1.1",
        "type": "ipaddress",
        "customer": 5
    }
]

#####################################################################################
# Utilities
#####################################################################################

def generate_default_config():
    config = configparser.ConfigParser()
    config.read_string(CATO_DEFAULT_CONFIGURATION)
    return config

#####################################################################################
# Fixtures
#####################################################################################

@pytest.fixture
def create_cli_arguments():
    def parse_parser(action="",noun="",subject=""):
        parser = catocli.setup_argument_parser()
        args = parser.parse_args([action, noun])

        # If you pass subject into parse_args, it produces a list instead of a string
        if subject:
            args.subject = subject

        return args

    return parse_parser

@pytest.fixture
def create_test_config_properties():
    return catocli.read_config_data(default_config_path)

@pytest.fixture
def create_basic_client():
    parser = catocli.setup_argument_parser()
    sampleArgs = parser.parse_args(["test","test"])
    config = catocli.read_config_data(default_config_path)
    return CATOClient(properties=config, arguments=sampleArgs)

#####################################################################################
# CLI Argument Fixtures
#####################################################################################

@pytest.fixture
def create_universal_cli_args():
    parser = catocli.setup_argument_parser()
    args = parser.parse_args(['',''])

    for attr in CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT:
        setattr(args, attr, CATO_DEFAULT_CONFIGURATION_ARGUMENTS_FORMAT[attr])

    testKeywords = copy.deepcopy(CATO_DEFAULT_CONFIGURATION_KEYWORDS_FORMAT)
    testKeywords['arguments'] = args
    testKeywords['properties'] = generate_default_config()

    return testKeywords