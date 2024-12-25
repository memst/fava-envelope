"""
This type stub file was generated by pyright.
"""

import unittest

"""
Unit tests for the Inventory class.
"""
__copyright__ = ...
__license__ = ...
P = ...
I = ...
def setUp(module): # -> None:
    ...

def tearDown(module): # -> None:
    ...

class TestInventory(unittest.TestCase):
    def checkAmount(self, inventory, number, currency): # -> None:
        ...
    
    def test_from_string(self): # -> None:
        ...
    
    def test_ctor_empty_len(self): # -> None:
        ...
    
    def test_str(self): # -> None:
        ...
    
    def test_copy(self): # -> None:
        ...
    
    def test_op_eq(self): # -> None:
        ...
    
    def test_op_lt(self): # -> None:
        ...
    
    def test_is_small__value(self): # -> None:
        ...
    
    def test_is_small__dict(self): # -> None:
        ...
    
    def test_is_small__with_default(self): # -> None:
        ...
    
    def test_is_mixed(self): # -> None:
        ...
    
    def test_is_reduced_by(self): # -> None:
        ...
    
    def test_op_neg(self): # -> None:
        ...
    
    def test_op_abs(self): # -> None:
        ...
    
    def test_op_mul(self): # -> None:
        ...
    
    def test_get_only_position(self): # -> None:
        ...
    
    def test_get_currency_units(self): # -> None:
        ...
    
    def test_segregate_units(self): # -> None:
        ...
    
    def test_split(self): # -> None:
        ...
    
    def test_units1(self): # -> None:
        ...
    
    POSITIONS_ALL_KINDS = ...
    def test_units(self): # -> None:
        ...
    
    def test_cost(self): # -> None:
        ...
    
    def test_average(self): # -> None:
        ...
    
    def test_currencies(self): # -> None:
        ...
    
    def test_currency_pairs(self): # -> None:
        ...
    
    def test_add_amount(self): # -> None:
        ...
    
    def test_add_amount__zero(self): # -> None:
        ...
    
    def test_add_amount__booking(self): # -> None:
        ...
    
    def test_add_amount__multi_currency(self): # -> None:
        ...
    
    def test_add_amount__withlots(self): # -> None:
        ...
    
    def test_add_amount__allow_negative(self): # -> None:
        ...
    
    def test_add_position(self): # -> None:
        ...
    
    def test_op_add(self): # -> None:
        ...
    
    def test_update(self): # -> None:
        ...
    
    def test_sum_inventories(self): # -> None:
        ...
    
    def test_reduce(self): # -> None:
        ...
    


if __name__ == '__main__':
    ...
