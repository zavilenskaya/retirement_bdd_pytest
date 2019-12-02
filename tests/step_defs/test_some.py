# coding=utf-8
"""calculate_retirement_age feature tests."""
from retirement_reattempt import *
from pytest_bdd import (
    parsers,
    given,
    scenario,
    then,
    when,
)
import pytest


EXTRA_TYPES = {'Number': int,
               'Text': str}

CONVERTERS = {
    'birth_year': int,
    'birth_month': int,
    'age_years': int,
    'age_month': int,
    'ret_year': int,
    'ret_month': int,
    'error_message': str
}


@scenario('../features/retirement.feature', 'Testing with 1959 birth year')
def test_with_1959_birth_year():
    """Testing with 1800 birth year."""
    pass

@given('calculate retirement age function')
def calculate_retirement_age_function():
    """calculate retirement age function."""
    pass

@when('the year of birth  "1959" is entered')
def the_year_of_birth_1959():
    pass

@then("results for age of retirement is '(66, 10)'")
def results():
    """results for age of retirement is 'Birth year "1800" must be no earlier than 1900'."""
    assert calculate_retirement_age(1959) == (66, 10)

##################Testing with 1800 birth year#############################
@scenario('../features/retirement.feature', 'Testing with 1800 birth year')
def test_with_1800_birth_year():
    pass

@given('calculate retirement age function')
def retirement_age():
    pass

@when('the year of birth  "1800" is entered')
def the_year_of_birth_1800():
    return 1800

@then("results for age of retirement is 'Birth year \"1800\" must be no earlier than 1900'")
def results():
    with pytest.raises(ValueError, match=r'Birth year "1800" must be no earlier than 1900'):
        calculate_retirement_age(the_year_of_birth_1800())

##################Testing with 3001 birth year#############################
@scenario('../features/retirement.feature', 'Testing with 3001 birth year')
def test_with_3001_birth_year():
    pass


@given('calculate retirement age function')
def retirement_age():
    pass


@when('the year of birth  "3001" is entered')
def the_year_of_birth_3001():
    return 3001


@then("results for age of retirement is 'Birth year \"3001\" must be earlier than 3000'")
def results():
    with pytest.raises(ValueError, match=r'Birth year "3001" must be earlier than 3000'):
        calculate_retirement_age(the_year_of_birth_3001())

##################Testing with 3000 birth year#############################
@scenario('../features/retirement.feature', 'Testing with 3001 birth year')
def test_with_3000_birth_year():
    pass


@given('calculate retirement age function')
def retirement_age():
    pass


@when('the year of birth  "3000" is entered')
def the_year_of_birth_3000():
    return 3000


@then("results for age of retirement is 'Birth year \"3000\" must be earlier than 3000'")
def results():
    with pytest.raises(ValueError, match=r'Birth year "3000" must be earlier than 3000'):
        calculate_retirement_age(the_year_of_birth_3000())


##################Testing with valid data retirement age#############################
@scenario('../features/retirement.feature', 'Testing with valid data age')
def test_with_valid_data():
    pass

@given('calculate retirement age function')
def calculate_retirement_age_function():
    pass


@when(parsers.cfparse('the year of birth "{birth_year:Number}" is entered', extra_types=EXTRA_TYPES))
@when('the year of birth "<birth_year>" is entered')
def the_year_of_birth(birth_year):
    return birth_year

@then(parsers.cfparse('results for age of retirement "{age_years:Number}", "{age_month:Number}" \
                        with "{birth_year:Number}"', extra_types=EXTRA_TYPES))
@then('results for age of retirement "<age_years>", "<age_month>" with "<birth_year>"')
def results(age_years, age_month, birth_year):
    assert calculate_retirement_age(birth_year) == (int(age_years), int(age_month))

######################Testing with valid data retirement date#######################
@scenario('../features/retirement.feature', 'Testing with valid data retirement_date')
def test_with_valid_data_date():
    pass


@given("calculate_retirement_date function")
def calculate_retirement_date_function():
    pass


@when(parsers.cfparse('the year of birth "{birth_year:Number}", month of birth "{birth_month:Number}", age of retirement "{age_years:Number}",month of retirement "{age_month:Number}" is entered', extra_types=EXTRA_TYPES))
@when('the year of birth "<birth_year>", month of birth "<birth_month>", age of retirement "<age_years>", month of retirement  "<age_month>" is entered')
def input_numbers(birth_year, birth_month, age_years, age_month):
    return birth_year, birth_month, age_years, age_month


@then(parsers.cfparse('results for year "{ret_year:Number}" and month of retirement "{ret_month:Number}" is returned with "{birth_year:Number}", "{birth_month:Number}", "{age_years:Number}", "{age_month:Number}"', extra_types=EXTRA_TYPES))
@then('results for year "<ret_year>" and month of retirement "<ret_month>"is returned, with "<birth_year>", "<birth_month>", "<age_years>", "<age_month>"')

def results(ret_year, ret_month, birth_year, birth_month, age_years, age_month, ):
    assert calculate_retirement_date(birth_year, birth_month, age_years, age_month) == (int(ret_year), int(ret_month))

######################Testing with valid data retirement date#######################
@scenario('../features/retirement.feature', 'Testing with invalid data retirement_date')
def test_with_invalid_data_date():
    pass


@given("calculate_retirement_date function")
def calculate_retirement_date_function():
    pass


@when(parsers.cfparse('the year of birth "{birth_year:Number}", month of birth "{birth_month:Number}", age of retirement "{age_years:Number}",month of retirement "{age_month:Number}" is entered', extra_types=EXTRA_TYPES))
@when('the year of birth "<birth_year>", month of birth "<birth_month>", age of retirement "<age_years>", month of retirement  "<age_month>" is entered ')
def input_numbers(birth_year, birth_month, age_years, age_month):
    return birth_year, birth_month, age_years, age_month


@then(parsers.cfparse('appropriate error message is returned "{error_message:Text}" with "{birth_year:Number}", "{birth_month:Number}", "{age_years:Number}", "{age_month:Number}"', extra_types=EXTRA_TYPES))
@then('appropriate error message is returned "<error_message>" with "<birth_year>", "<birth_month>", "<age_years>", "<age_month>"')
def results(error_message, birth_year, birth_month, age_years, age_month):
    #assert calculate_retirement_date(birth_year, birth_month, age_years, age_month) == error_message
    with pytest.raises(ValueError, match=error_message.strip("'")):
        calculate_retirement_date(birth_year, birth_month, age_years, age_month)
