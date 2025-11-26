from src.utils import is_number

def test_is_number():
    assert is_number("10") == True
    assert is_number("42") == True
    assert is_number("-5") == True
    assert is_number("abc") == False
    assert is_number("12.5") == False
