import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# --- Тесты для capitalize ---
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("123abc", "123abc"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.error
@pytest.mark.parametrize("input_str", [
    None,
    123,
    ["not", "a", "string"],
])
def test_capitalize_errors(input_str):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.capitalize(input_str)


# --- Тесты для trim ---
@pytest.mark.error
@pytest.mark.parametrize("input_str", [
    None,
    123.45,
    {"key": "value"},
])
def test_trim_errors(input_str):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.trim(input_str)


# --- Тесты для to_list ---
@pytest.mark.error
@pytest.mark.parametrize("input_str, delimiter", [
    (None, ","),
    ("a,b,c", None),
    (123, ";"),
])
def test_to_list_errors(input_str, delimiter):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.to_list(input_str, delimiter)


@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("04 апреля 2023", " ", ["04", "апреля", "2023"]),
    ("апрель|2023", "|", ["апрель", "2023"]),
])
def test_to_list_dates(input_str, delimiter, expected):
    assert string_utils.to_list(input_str, delimiter) == expected


# --- Тесты для contains ---
@pytest.mark.error
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
    ("hello", None),
    (123, "1"),
])
def test_contains_errors(string, symbol):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.contains(string, symbol)
