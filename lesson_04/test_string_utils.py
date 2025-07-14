import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_string, expected_string', [
    ('python', 'Python'),
    ('Python', 'Python'),
    ('be yourself!', 'Be yourself!'),
    ('157kms', '157kms'),
    ('!attention', '!attention'),
    (pytest.param('SkyPro', 'SkyPro',
                  marks=pytest.mark.xfail(reason="Баг 1: input='SkyPro'")))
])
def test_capitalize_positive(input_string, expected_string):
    assert string_utils.capitalize(input_string) == expected_string


@pytest.mark.negative
@pytest.mark.parametrize('input_string, expected_string', [
    ('', ''),
    (' ', ' ')
])
def test_capitalise_negative(input_string, expected_string):
    assert string_utils.capitalize(input_string) == expected_string


@pytest.mark.positive
@pytest.mark.parametrize('input_string, expected_string', [
    ('SkyPro', 'SkyPro'),
    (' SkyPro', 'SkyPro'),
    ('SkyPro ', 'SkyPro '),
    ('  SkyPro', 'SkyPro'),
    ('Dream big, work hard', 'Dream big, work hard')
])
def test_trim_positive(input_string, expected_string):
    assert string_utils.trim(input_string) == expected_string


@pytest.mark.negative
@pytest.mark.parametrize('input_string, expected_string', [
    ('', ''),
    (' ', ''),
    ('   ', ''),
    ('125', '125')
])
def test_trim_negative(input_string, expected_string):
    assert string_utils.trim(input_string) == expected_string


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected_result', [
    ('SkyPro', 'S', True),
    (pytest.param('SkyPro', 's', True,
                  marks=pytest.mark.xfail(reason="баг 2: регистр символа"))),
    ('Dream big, work hard', " ", True)
])
def test_contains_positive(string, symbol, expected_result):
    assert string_utils.contains(string, symbol) == expected_result


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, expected_result', [
    ('SkyPro', 'W', False),
    ('123', '1', True),
    ('123', '10', False),
    ('', 'a', False),
    ('', '', True)
])
def test_contains_negative(string, symbol, expected_result):
    assert string_utils.contains(string, symbol) == expected_result


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected_result', [
    ('SkyPro', 'k', 'SyPro'),
    ('hot, very hot', 'hot', ', very '),
    ('SkyPro', 'Pro', 'Sky'),
    (pytest.param('SkyPro', 'sky', 'Pro',
                  marks=pytest.mark.xfail(reason="баг 3: регистр символов"))),
    ('Dream big, work hard', ' ', 'Dreambig,workhard'),
    ('Dream big, work hard', 'work hard', 'Dream big, '),
    ('Dream big, work hard', 'work hard', 'Dream big, '),
    ('a', 'a', '')
])
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, expected_result', [
    ('', 'a', ''),
    ('', '', ''),
    ('123', '10', '123'),
    ('123', '1', '23')
])
def test_delete_symbol_negative(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
