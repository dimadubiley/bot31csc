import pytest
from calculator import analyze_text

def test_empty_string():
    assert analyze_text("") == {
        "digits": 0, "letters": 0, "upper": 0, "lower": 0, "symbols": 0
    }

def test_only_digits():
    assert analyze_text("12345")["digits"] == 5
    assert analyze_text("12345")["symbols"] == 0

def test_only_letters_lower():
    res = analyze_text("abcde")
    assert res["letters"] == 5
    assert res["lower"] == 5
    assert res["upper"] == 0

def test_only_letters_upper():
    res = analyze_text("ABCDE")
    assert res["letters"] == 5
    assert res["upper"] == 5
    assert res["lower"] == 0

def test_mixed_letters():
    res = analyze_text("AbCdE")
    assert res["upper"] == 3
    assert res["lower"] == 2

def test_symbols_only():
    res = analyze_text("!@#$%^&*()")
    assert res["symbols"] == 10
    assert res["letters"] == 0
    assert res["digits"] == 0

def test_mixed_all():
    res = analyze_text("Aa1!Bb2?")
    assert res["digits"] == 2
    assert res["letters"] == 4
    assert res["symbols"] == 2

def test_spaces_count_as_symbols():
    assert analyze_text("a b c")["symbols"] == 2  # два пробіли

def test_unicode_letters():
    res = analyze_text("Привіт123!")
    assert res["letters"] == 6
    assert res["digits"] == 3
    assert res["symbols"] == 1

def test_long_complex_text():
    txt = "Hello123!! World_2025"
    res = analyze_text(txt)
    assert res["digits"] == 7
    assert res["letters"] == 12
    assert res["symbols"] == 4
