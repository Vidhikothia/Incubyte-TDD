import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0
