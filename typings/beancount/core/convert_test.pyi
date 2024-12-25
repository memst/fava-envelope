"""
This type stub file was generated by pyright.
"""

import unittest
from beancount import loader

"""Unit tests for conversion functions.
"""
__copyright__ = ...
__license__ = ...
def build_price_map_util(date_currency_price_tuples): # -> PriceMap:
    """Build a partial price-map just for testing.

    Args:
      date_currency_price_tuples: A list of (datetime.date, currency-string,
        price-Amount) tuples to fill in the database with.
    Returns:
      A price_map, as per build_price_map().
    """
    ...

class TestPositionConversions(unittest.TestCase):
    """Test conversions to units, cost, weight and market-value for Position objects."""
    def test_units(self): # -> None:
        ...
    
    def test_cost__empty(self): # -> None:
        ...
    
    def test_cost__not_empty(self): # -> None:
        ...
    
    def test_cost__missing(self): # -> None:
        ...
    
    def test_weight__no_cost(self): # -> None:
        ...
    
    def test_weight__with_cost(self): # -> None:
        ...
    
    def test_weight__with_cost_missing(self): # -> None:
        ...
    
    def test_old_test(self): # -> None:
        ...
    
    PRICE_MAP_EMPTY = ...
    PRICE_MAP_HIT = ...
    def test_value__no_currency(self): # -> None:
        ...
    
    def test_value__currency_from_cost(self): # -> None:
        ...
    
    def test_convert_position__success(self): # -> None:
        ...
    
    def test_convert_position__miss_but_same_currency(self): # -> None:
        ...
    
    def test_convert_position__miss_and_miss_rate_to_rate(self): # -> None:
        ...
    
    PRICE_MAP_RATEONLY = ...
    def test_convert_position__miss_and_miss_value_rate(self): # -> None:
        ...
    
    def test_convert_position__miss_and_miss_both(self): # -> None:
        ...
    
    def test_convert_position__miss_and_success_on_implieds(self): # -> None:
        ...
    
    def test_convert_amount__fail(self): # -> None:
        ...
    
    def test_convert_amount__success(self): # -> None:
        ...
    
    def test_convert_amount__noop(self): # -> None:
        ...
    
    @loader.load_doc()
    def test_convert_amount_with_date(self, entries, _, __): # -> None:
        """
        2013-01-01 price  USD  1.20 CAD
        2014-01-01 price  USD  1.25 CAD
        2015-01-01 price  USD  1.30 CAD
        """
        ...
    


class TestPostingConversions(TestPositionConversions):
    """Test conversions to units, cost, weight and market-value for Posting objects."""
    def test_weight_with_cost_and_price(self): # -> None:
        ...
    
    def test_weight_with_only_price(self): # -> None:
        ...
    
    def test_value__currency_from_price(self): # -> None:
        ...
    
    def test_convert_position__currency_from_price(self): # -> None:
        ...
    


class TestMarketValue(unittest.TestCase):
    @loader.load_doc()
    def setUp(self, entries, _, __): # -> None:
        """
        2013-06-01 price  USD  1.01 CAD
        2013-06-05 price  USD  1.05 CAD
        2013-06-06 price  USD  1.06 CAD
        2013-06-07 price  USD  1.07 CAD
        2013-06-10 price  USD  1.10 CAD

        2013-06-01 price  HOOL  101.00 USD
        2013-06-05 price  HOOL  105.00 USD
        2013-06-06 price  HOOL  106.00 USD
        2013-06-07 price  HOOL  107.00 USD
        2013-06-10 price  HOOL  110.00 USD

        2013-06-01 price  AAPL  91.00 USD
        2013-06-05 price  AAPL  95.00 USD
        2013-06-06 price  AAPL  96.00 USD
        2013-06-07 price  AAPL  97.00 USD
        2013-06-10 price  AAPL  90.00 USD
        """
        ...
    
    def test_no_change(self): # -> None:
        ...
    
    def test_other_currency(self): # -> None:
        ...
    
    def test_mixed_currencies(self): # -> None:
        ...
    
    def test_stock_single(self): # -> None:
        ...
    
    def test_stock_many_lots(self): # -> None:
        ...
    
    def test_stock_different_ones(self): # -> None:
        ...
    
    def test_stock_not_found(self): # -> None:
        ...
    


if __name__ == '__main__':
    ...
