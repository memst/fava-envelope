"""
This type stub file was generated by pyright.
"""

import unittest

__copyright__ = ...
__license__ = ...
def decimalize(number_list): # -> list[Any]:
    ...

class DisplayContextBaseTest(unittest.TestCase):
    alignment = ...
    def assertFormatNumbers(self, number_strings, expected_fmt_numbers, **build_args): # -> None:
        ...
    


class TestDisplayContext(DisplayContextBaseTest):
    def test_dump(self): # -> None:
        ...
    


class TestDisplayContextNatural(DisplayContextBaseTest):
    alignment = ...
    def test_natural_uninitialized(self): # -> None:
        ...
    
    def test_natural_no_clear_mode(self): # -> None:
        ...
    
    def test_natural_clear_mode(self): # -> None:
        ...
    
    def test_natural_maximum(self): # -> None:
        ...
    
    def test_natural_commas(self): # -> None:
        ...
    
    def test_natural_reserved(self): # -> None:
        ...
    


class TestDisplayContextRight(DisplayContextBaseTest):
    alignment = ...
    def test_right_uninitialized(self): # -> None:
        ...
    
    def test_right_sign(self): # -> None:
        ...
    
    def test_right_integer(self): # -> None:
        ...
    
    def test_right_integer_commas(self): # -> None:
        ...
    
    def test_right_fractional(self): # -> None:
        ...
    
    def test_right_fractional_commas(self): # -> None:
        ...
    


class TestDisplayContextDot(DisplayContextBaseTest):
    alignment = ...
    def test_dot_uninitialized(self): # -> None:
        ...
    
    def test_dot_basic(self): # -> None:
        ...
    
    def test_dot_basic_multi(self): # -> None:
        ...
    
    def test_dot_sign(self): # -> None:
        ...
    
    def test_dot_integer(self): # -> None:
        ...
    
    def test_dot_integer_commas(self): # -> None:
        ...
    
    def test_dot_fractional(self): # -> None:
        ...
    
    def test_dot_fractional_commas(self): # -> None:
        ...
    


class TestDisplayContextQuantize(unittest.TestCase):
    def test_quantize_basic(self): # -> None:
        ...
    


if __name__ == '__main__':
    ...
