import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import add

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("5") == 5

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_newline_between_numbers():
    assert add("1\n2,3") == 6

def test_custom_delimiter_semicolon():
    assert add("//;\n1;2") == 3

def test_negative_number():
    with pytest.raises(Exception) as e:
        add("1,-2,3")
    assert str(e.value) == "negative numbers not allowed -2"    

def test_multiple_negative_numbers():
    with pytest.raises(Exception) as e:
        add("-1,2,-3,-4")
    assert str(e.value) == "negative numbers not allowed -1,-3,-4"

def test_custom_delimiter_no_numbers():
    assert add("//;\n") == 0

def test_ignore_large_numbers():
    assert add("2,1001") == 2

def test_delimiter_any_length():
    assert add("//[***]\n1***2***3") == 6

def test_multiple_delimiters():
    assert add("//[*][%]\n1*2%3") == 6
