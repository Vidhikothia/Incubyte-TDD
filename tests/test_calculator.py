import sys
import os
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
