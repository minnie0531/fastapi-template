import pytest
import json
import os

"""
This file is for unit test of a service.
It compares input_data.json in test_data directory to each result.

This is the example of documentation for this unit test

Input data :
    Selected arguments from the existing application

Result :
   SQL queirs which are used in Exdata
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
