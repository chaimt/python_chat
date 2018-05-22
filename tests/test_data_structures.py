import pytest
from domain.data_structures import MessageApp


@pytest.fixture
def client():
    messages = MessageApp()
    assert messages.total_sent() == 0
