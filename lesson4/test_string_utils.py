import pytest

from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize('string, result', [
    # позитивные
    ("skypro", "Skypro"),
    ("margaRita", "Margarita"),
    ("MargaRita", "Margarita"),
    ("peter 1", "Peter 1"),
    #негативные
    ("", ""),
    ("URL", "Url"),
    (" skypro", " skypro")
])
def test_capitilize(string, result):
    string_util = StringUtils()
    res = string_util.capitilize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [
    #позитивные
    (" cat", "cat"),
    (" ABC", "ABC"),
    ("  skypro", "skypro"),
    (" Peter 1 ", "Peter 1 "),
    #негативные
    ("", ""),
    ("ca t", "ca t")
])
def test_trim(string, result):
    string_util = StringUtils()
    assert string_util.trim(string) == result


@pytest.mark.parametrize('string, delimeter, result', [
    #позитивные
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    ("1/n2/n3", "/n", ["1", "2", "3"]),
    ("one:two:three", ":", ["one", "two", "three"]),
    #негативные
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"])
])
def test_to_list(string, delimeter, result):
    string_utils = StringUtils()
    if delimeter is None:
        res = string_utils.to_list(string)
    else:
        res = string_utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #позитивные
    ("five", "f", True),
    (" two", "t", True),
    ("sleep  ", "e", True),
    ("Anna-Maria", "-", True),
    ("123", "1", True),
    ("GPS", "P", True),
    ("", "", True),
    #негативные
    ("morning", "M", False),
    ("Morning", "m", False),
    ("morning", "y", False),
    ("morning", "&", False),
    ("", "m", False)
])
def test_contains(string, symbol, result):
    string_util = StringUtils()
    res = string_util.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #позитивные
    ("lesson", "s", "leon"),
    ("lesson", "on", "less"),
    ("Anna-Maria", "-", "AnnaMaria"),
    ("Anna Maria", " ", "AnnaMaria"),
    ("123", "1", "23"),
    #негативные
    ("", "", ""),
    ("", "m", ""),
    ("lesson", "z", "lesson"),
    ("lesson ", " ", "lesson")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #позитивные
    ("morning", "m", True),
    ("", "", True),
    ("Morning", "M", True),
    (" morning", " ", True),
    ("-morning", "-", True),
    #негативные
    ("morning", "M", False),
    ("Morning", "m", False),
    ("morning ", " ", False),
    ("morning-", "-", False),
    ("morning", "1", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #позитивные
    ("morning", "g", True),
    ("morning ", " ", True),
    ("GPS", "S", True),
    ("", "", True),
    ("Peter 1", "1", True),
    #негативные
    ("morning", "n", False),
    ("morning", "G", False),
    ("123", "m", False),
    ("morning", " ", False),
    (" ", "m", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [
    #позитивные
    ("", True),
    (" ", True),
    ("  ", True),
    #негативные
    ("123", False),
    (" soon", False),
    ("S", False),
    ("+", False)
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result


@pytest.mark.parametrize('lst, joiner, result', [
    #позитивные
    (["a", "b", "c"], "/", "a/b/c"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["A", "B", "C"], "-", "A-B-C"),
    (["a", "b", "c"], " ", "a b c"),
    #негативные
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    assert res == result
