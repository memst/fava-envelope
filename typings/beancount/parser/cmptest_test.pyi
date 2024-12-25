"""
This type stub file was generated by pyright.
"""

import unittest
from beancount.parser import cmptest

"""
Tests for cmptest base test class.
"""
__copyright__ = ...
__license__ = ...
class TestCompareTestFunctions(unittest.TestCase):
    def test_read_string_or_entries(self): # -> None:
        ...
    
    def test_local_booking(self): # -> None:
        ...
    


class TestTestCase(cmptest.TestCase):
    ledger_text = ...
    def setUp(self): # -> None:
        ...
    
    def test_assertEqualEntries(self): # -> None:
        ...
    
    def test_assertIncludesEntries(self): # -> None:
        ...
    
    def test_assertExcludesEntries(self): # -> None:
        ...
    


if __name__ == '__main__':
    ...
