"""
Basic smoke test for project setup.
"""
from src.main import get_welcome_message


def test_welcome_message():
    message = get_welcome_message()
    assert "SahkaarX" in message
    assert len(message) > 0
