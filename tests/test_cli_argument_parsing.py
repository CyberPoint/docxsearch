import numpy as np
import os
import pytest

import scripts.catocli as catocli

def test_can_read_arguments(create_cli_arguments):
    sampleArgs = create_cli_arguments(action="list", noun="customer", subject="1,2")
    assert sampleArgs.action == "list"
    assert sampleArgs.noun == "customer"
    assert sampleArgs.subject == "1,2"
