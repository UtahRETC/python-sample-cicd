import pytest
from src.app import app


client = app.test_client()


def test_greet_with_default_parameters():
    response = client.get("/greet")
    assert response.json.get("message") == "Hello friend"


def test_greet_with_a_name_parameter():
    response = client.get("/greet?name=Ahmed")
    assert response.json.get("message") == "Hello Ahmed"


def test_greet_with_a_greeting_parameter():
    response = client.get("/greet?greeting=Morning")
    assert response.json.get("message") == "Morning friend"


def test_greet_with_all_parameters():
    response = client.get("/greet?name=Ahmed&greeting=Morning")
    assert response.json.get("message") == "Morning Ahmed"
