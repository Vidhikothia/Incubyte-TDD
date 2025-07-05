import sys
import os
import pytest

# Add src directory to path so we can import calculator.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import add

# Basic Tests 

def test_empty_string():
    # Empty input should return 0
    assert add("") == 0

def test_single_number():
    # Single number input should return the number itself
    assert add("5") == 5

def test_two_numbers():
    # Two comma-separated numbers should return their sum
    assert add("1,2") == 3

def test_multiple_numbers():
    # Any number of comma-separated numbers should return their total
    assert add("1,2,3,4,5") == 15

# Newline & Delimiter Handling

def test_newline_between_numbers():
    # Newlines can also act as delimiters
    assert add("1\n2,3") == 6

def test_custom_delimiter_semicolon():
    # Custom delimiter: semicolon
    assert add("//;\n1;2") == 3

def test_custom_delimiter_no_numbers():
    # Custom delimiter defined but no numbers provided
    assert add("//;\n") == 0

# Negative Number Handling

def test_negative_number():
    # Single negative number should raise an exception
    with pytest.raises(Exception) as e:
        add("1,-2,3")
    assert str(e.value) == "negative numbers not allowed -2"

def test_multiple_negative_numbers():
    # All negative numbers should be listed in exception
    with pytest.raises(Exception) as e:
        add("-1,2,-3,-4")
    assert str(e.value) == "negative numbers not allowed -1,-3,-4"

# Special Cases

def test_ignore_large_numbers():
    # Numbers > 1000 should be ignored
    assert add("2,1001") == 2

def test_delimiter_any_length():
    # Delimiter can be longer than one character
    assert add("//[***]\n1***2***3") == 6

def test_multiple_delimiters():
    # Multiple single-character delimiters supported
    assert add("//[*][%]\n1*2%3") == 6

def test_multiple_long_delimiters():
    # Multiple delimiters with length > 1 supported
    assert add("//[***][%%]\n1***2%%3") == 6
