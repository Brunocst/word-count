import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.api import app, WORD_MAX_LEN
from fastapi.testclient import TestClient
from bs4 import BeautifulSoup


@pytest.fixture
def test_client():
    return TestClient(app)

@pytest.fixture
def samples():
    return {
        "count": "This is a test for the word count function",
        "multiline": "How are you doing ? \n I am doing great",
        "long_text": "T"*(WORD_MAX_LEN+1),
        "numbers": "How are you doing ? I am doing great 3 4 and you ? 1",
        "emoji": "How are you doing ? I am doing great and you ? \U0001F43F",
        "special_char": "How are you doing? I am doing great and you?",
        "delimiter": "How-are-you-doing",
        "empty": ""
    }

def error_checker_helper(response, count=None):
    
    parsed_response = BeautifulSoup(response.text, "html.parser")
    res_div = parsed_response.find("div", class_="result")

    assert res_div is not None 
    assert f"Word count: {count}" in res_div.text


def test_main(test_client):
    response = test_client.get("/")
    assert response.status_code == 200

def test_count_words(test_client, samples):
    response = test_client.post(
        "/",
        data = {"text": samples["count"]}
    )

    assert response.status_code == 200
    error_checker_helper(response, 9)


def test_count_multiline(test_client, samples):
    response = test_client.post(
        "/",
        data = {"text": samples["multiline"]}
    )

    assert response.status_code == 200
    error_checker_helper(response, 8)


def test_count_with_numbers(test_client, samples):
    response = test_client.post(
        "/",
        data = {"text": samples["numbers"]}
    )

    assert response.status_code == 200
    error_checker_helper(response, 10)


def test_count_long_words(test_client, samples):
    response = test_client.post(
        "/",
        data = {"text": samples["long_text"]}
    )

    parsed_response = BeautifulSoup(response.text, "html.parser")
    res_div = parsed_response.find("div", class_="error")

    assert response.status_code == 200
    assert res_div is not None 
    assert f"The input is too long (max {WORD_MAX_LEN} characters)" in res_div.text

def test_count_words_emoji(test_client, samples):
    response = test_client.post(
        "/",
        data = {"text": samples["emoji"]}
    )

    assert response.status_code == 200
    error_checker_helper(response, 10)

def test_count_hyphen_delimiter(test_client, samples):
    response = test_client.post(
        "/",
        data = {"text": samples["delimiter"]}
    )

    assert response.status_code == 200
    error_checker_helper(response, 4)


def test_empty_words(test_client, samples):
    response = test_client.post(
        "/",
        data = {"text": samples["empty"]}
    )

    parsed_response = BeautifulSoup(response.text, "html.parser")
    res_div = parsed_response.find("div", class_="error")

    assert response.status_code == 200
    assert res_div is not None 
    assert "A text input is required" in res_div.text

