import pytest
from pytest_bdd import scenarios, scenario, given, when, then

scenarios("../features/SumOfTwoArguments.feature")

@pytest.fixture
def result():
    return {"result": 0}
@pytest.fixture
def save_first_argument():
    return {"first_argument": 0}
@pytest.fixture
def save_second_argument():
    return {"second_argument": 0}

@given("I have entered 2 into the calculator")
def add(save_first_argument):
    save_first_argument["first_argument"] += 2


@given("I have entered 2 into the calculator")
def add(save_second_argument):
    save_second_argument["second_argument"] += 2


@when("I press add")
def press_button(result):
    result["result"] += 4

@then("the result should be 4 on the screen")
def result_should_be(result):
    assert result["result"] == 4