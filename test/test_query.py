import pytest
import json
import os

"""
This file is to unit test query builder.
It compares input_data.json in test_data directory to each result.
Query build build queries based on its own arguements.
"""

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def read_input():
    with open(dir_path + "/test_data/input_data.json") as f:
        input = json.load(f)
        return input


def test_one(read_input):
    with open(dir_path + "/test_data/result1.json") as f:
        result = json.load(f)

    assert result["data"] == read_input["1"]


def test_owo(read_input):
    with open(dir_path + "/test_data/result2.json") as f:
        result = json.load(f)

    assert result["data"] == read_input["2"]
