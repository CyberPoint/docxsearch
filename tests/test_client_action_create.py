import configparser
import copy
import pytest

from catocli.catoclient import CATOClient
from unittest.mock import patch

#####################################################################################
# Setup
#####################################################################################

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

def augment_arguments_with_dict(keywordObject, argsDict):
    for attr in argsDict:
        setattr(keywordObject['arguments'], attr, argsDict[attr])
    return keywordObject

#####################################################################################
# Test Cases
#####################################################################################

def test_create_operation_payload_check(create_universal_cli_args):
    
    ####
    # Configure actions
    ####

    #./catocli create operation 10.0.1.1 --campaign=23 "--template=Ping (Basic Ping)" --customer=5
    # Arguments are received as strings; defining as integers to bypass some check validators.
    arguments = {
        'action':'create',
        'noun':'operation',
        'subject':414, # 10.0.1.1
        'campaign':23,
        'customer': 5,
        'template':134  # Ping (Basic Ping)
    }

    testKeywords = augment_arguments_with_dict(create_universal_cli_args, arguments)
    client = CATOClient(**testKeywords)
    client.needs_login = False # Do this to force skipping the auth process

    ####
    # /Configure actions
    ####

    testPayload = client.create_action_payload_generator()
    
    for attr in ['campaign', 'customer', 'template']:
        assert testPayload[attr] == arguments[attr]

#######
# Additional test cases to handle later
#######

# #./catocli create operations 192.168.1.3,10.0.1.1 -c 5 -f json -j '{"target":406,"campaign":23,"template":134,"reasoning":"New operation requested."}'
# # ^ should make a ping op for targets 413,414; not 406
# arguments = {
#     'action':'create',
#     'noun':'operations',
#     'subject':'192.168.1.3,10.0.1.1',
#     'customer':'5',
#     'json':'{"target":406,"campaign":23,"template":134,"reasoning":"New operation requested."}'
# }

# #./catocli create operation 192.168.1.3,10.0.1.1 -c 5 -f json -j '{"target":406,"campaign":23,"template":134,"reasoning":"New operation requested."}'
# # ^ should fail due to noun being singular and it not parsing out the multiple objects
# # Note: There are location targets that have a ',' in their value which will break multi-target parsing
# arguments = {
#     'action':'create',
#     'noun':'operation',
#     'subject':'192.168.1.3,10.0.1.1',
#     'customer':'5',
#     'json':'{"target":406,"campaign":23,"template":134,"reasoning":"New operation requested."}'
# }

# #./catocli create operation -c 5 -f json -j '{"target":406,"campaign":23,"template":134,"reasoning":"New operation requested."}'
# # ^ should fail due to missing subject; yes it has the target specified in the json body
# arguments = {
#     'action':'create',
#     'noun':'operation',
#     'subject':'',
#     'customer':'5',
#     'json':'{"target":406,"campaign":23,"template":134,"reasoning":"New operation requested."}'
# }

# #./catocli create operation 10.0.1.1 --campaign=23 "--template=Ping (Basic Ping)" --customer=5
# # ^ should work just fine
# arguments = {
#     'action':'create',
#     'noun':'operation',
#     'subject':'10.0.1.1',
#     'campaign':'23',
#     'customer': '5',
#     'template':'Ping (Basic Ping)'
# }

# #./catocli create operations 192.168.1.1,192.168.1.3 -c 5 -f json -j '{"campaign":23,"template":134,"reasoning":"New operation requested."}'
# # ^ should also work just fine
# arguments = {
#     'action':'create',
#     'noun':'operations',
#     'subject':'192.168.1.1,192.168.1.3',
#     'customer':'5',
#     'json':'{"campaign":23,"template":134,"reasoning":"New operation requested."}'
# }

# # to-do: add test case without campaign to test if autocampaign creation gets triggered
# arguments = {
#     'action':'create',
#     'noun':'operation',
#     'subject':'192.168.1.1',
#     'customer':'5',
#     'json':'{"template":134,"reasoning":"New operation requested."}'
# }

# # to-do: following should fail; ambiguous since there's no customer or campaign specified. 
# # Could only work if the target value is unique
# arguments = {
#     'action':'create',
#     'noun':'operation',
#     'subject':'192.168.1.1',
#     'json':'{"template":134,"reasoning":"New operation requested."}'
# }