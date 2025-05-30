"""
This type stub file was generated by pyright.
"""

import unittest
from beancount.parser import cmptest
from beancount import loader

__copyright__ = ...
__license__ = ...
class TestPriceEntries(cmptest.TestCase):
    @loader.load_doc()
    def test_get_last_price_entries(self, entries, _, __): # -> None:
        """
        2013-01-01 price  USD  1.01 CAD
        2013-02-01 price  USD  1.02 CAD
        2013-03-01 price  USD  1.03 CAD
        2013-04-01 price  USD  1.04 CAD
        2013-05-01 price  USD  1.05 CAD
        2013-06-01 price  USD  1.06 CAD
        2013-07-01 price  USD  1.07 CAD
        """
        ...
    


class TestPriceMap(unittest.TestCase):
    def test_normalize_base_quote(self): # -> None:
        ...
    
    @loader.load_doc()
    def test_build_price_map(self, entries, _, __): # -> None:
        """
        2013-06-01 price  USD  1.10 CAD

        ;; Try some prices at the same date.
        2013-06-02 price  USD  1.11 CAD
        2013-06-02 price  USD  1.12 CAD
        2013-06-02 price  USD  1.13 CAD

        ;; One after too.
        2013-06-03 price  USD  1.14 CAD

        ;; Try a few inverse prices.
        2013-06-05 price  CAD  0.86956 USD
        2013-06-06 price  CAD  0.86207 USD
        """
        ...
    
    @loader.load_doc()
    def test_build_price_map_zero_prices(self, entries, _, __): # -> None:
        """
        1999-12-27 commodity EFA
        2010-10-01 price EFA                                 57.53 EFA
        2010-11-01 price EFA                                     0 EFA
        2011-03-01 price EFA                                 60.69 EFA
        """
        ...
    
    @loader.load_doc()
    def test_lookup_price_and_inverse(self, entries, _, __): # -> None:
        """
        2013-06-01 price  USD  1.01 CAD
        """
        ...
    
    @loader.load_doc()
    def test_get_all_prices(self, entries, _, __): # -> None:
        """
        2013-06-01 price  USD  1.01 CAD
        2013-06-03 price  USD  1.03 CAD
        2013-06-05 price  USD  1.05 CAD
        2013-06-07 price  USD  1.07 CAD
        2013-06-09 price  USD  1.09 CAD
        2013-06-11 price  USD  1.11 CAD
        """
        ...
    
    @loader.load_doc()
    def test_get_latest_price(self, entries, _, __): # -> None:
        """
        2013-06-01 price  USD  1.01 CAD
        2013-06-09 price  USD  1.09 CAD
        2013-06-11 price  USD  1.11 CAD
        """
        ...
    
    @loader.load_doc()
    def test_get_price(self, entries, _, __): # -> None:
        """
        2013-06-01 price  USD  1.00 CAD
        2013-06-10 price  USD  1.50 CAD
        2013-07-01 price  USD  2.00 CAD
        """
        ...
    
    @loader.load_doc()
    def test_ordering_same_date(self, entries, _, __): # -> None:
        """
        ;; The last one to appear in the file should be selected.
        2013-06-02 price  USD  1.13 CAD
        2013-06-02 price  USD  1.12 CAD
        2013-06-02 price  USD  1.11 CAD
        """
        ...
    
    @loader.load_doc()
    def test_project(self, entries, _, __): # -> None:
        """
        2013-06-01 price  USD      1.12 CAD
        2013-06-15 price  HOOL  1000.00 USD
        2013-06-15 price  MFFT   200.00 USD

        2013-07-01 price  USD      1.13 CAD
        2013-07-15 price  HOOL  1010.00 USD
        """
        ...
    
    @loader.load_doc()
    def test_project_missing(self, entries, _, __): # -> None:
        """
        2013-06-15 price  HOOL  1000.00 USD
        2013-07-01 price  USD      1.12 CAD
        2013-07-15 price  HOOL  1100.00 USD
        """
        ...
    
    @loader.load_doc()
    def test_project_collisions(self, entries, _, __): # -> None:
        """
        2013-06-01 price  USD      1.12 CAD
        2013-06-15 price  HOOL  1000.00 USD
        2013-06-15 price  HOOL  1125.00 CAD
        """
        ...
    


if __name__ == '__main__':
    ...
