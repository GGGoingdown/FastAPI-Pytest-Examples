import pytest
from src.utils import long_running_task, generate_greeting

@pytest.mark.unfinished
def test_long_running_task(mocker):
    # mocker.patch('time.sleep', return_value=None)
    result = long_running_task(sleep_time=1)
    assert result == "ok"


@pytest.mark.finished
def test_generate_greeting():
    name = "peter"
    greeting_message = generate_greeting(name)
    assert greeting_message == "Hello, peter"