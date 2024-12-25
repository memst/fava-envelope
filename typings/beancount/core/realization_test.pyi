"""
This type stub file was generated by pyright.
"""

import unittest
from beancount.utils import test_utils
from beancount import loader

"""Unit tests for realizations.
"""
__copyright__ = ...
__license__ = ...
def create_simple_account(): # -> RealAccount:
    ...

def create_real(account_value_pairs): # -> RealAccount:
    ...

class TestRealAccount(unittest.TestCase):
    def test_ctor(self): # -> None:
        ...
    
    def test_str(self): # -> None:
        ...
    
    def test_equality(self): # -> None:
        ...
    
    def test_getitem_setitem(self): # -> None:
        ...
    
    def test_setitem_constraints(self): # -> None:
        ...
    
    def test_clone(self): # -> None:
        ...
    


class TestRealGetters(unittest.TestCase):
    def test_get(self): # -> None:
        ...
    
    def test_get_or_create(self): # -> None:
        ...
    
    def test_contains(self): # -> None:
        ...
    
    def test_iter_children(self): # -> None:
        ...
    


class TestRealization(unittest.TestCase):
    @loader.load_doc()
    def test_postings_by_account(self, entries, errors, _): # -> None:
        """
        option "plugin_processing_mode" "raw"

        2012-01-01 open Expenses:Restaurant
        2012-01-01 open Expenses:Movie
        2012-01-01 open Assets:Cash
        2012-01-01 open Liabilities:CreditCard
        2012-01-01 open Equity:Opening-Balances

        2012-01-15 pad Liabilities:CreditCard Equity:Opening-Balances

        2012-03-01 * "Food"
          Expenses:Restaurant     100 CAD
          Assets:Cash            -100 CAD

        2012-03-10 * "Food again"
          Expenses:Restaurant      80 CAD
          Liabilities:CreditCard  -80 CAD

        ;; Two postings on the same account.
        2012-03-15 * "Two Movies"
          Expenses:Movie           10 CAD
          Expenses:Movie           10 CAD
          Liabilities:CreditCard  -20 CAD

        2012-03-20 note Liabilities:CreditCard "Called Amex, asked about 100 CAD dinner"

        2012-03-28 document Liabilities:CreditCard "march-statement.pdf"

        2013-04-01 balance Liabilities:CreditCard   204 CAD

        2014-01-01 close Liabilities:CreditCard
        """
        ...
    
    def test_realize_empty(self): # -> None:
        ...
    
    def test_realize_min_accoumts(self): # -> None:
        ...
    
    @loader.load_doc()
    def test_simple_realize(self, entries, errors, options_map): # -> None:
        """
          2013-05-01 open Assets:US:Checking:Sub   USD
          2013-05-01 open Expenses:Stuff
          2013-05-02 txn "Testing!"
            Assets:US:Checking:Sub            100 USD
            Expenses:Stuff           -100 USD
        """
        ...
    
    def test_realize(self): # -> None:
        ...
    


class TestRealFilter(unittest.TestCase):
    def test_filter_to_empty(self): # -> None:
        ...
    
    def test_filter_almost_all(self): # -> None:
        ...
    
    def test_filter_with_leaves(self): # -> None:
        ...
    
    def test_filter_no_leaves(self): # -> None:
        ...
    
    def test_filter_misc(self): # -> None:
        ...
    


class TestRealOther(test_utils.TestCase):
    @loader.load_doc()
    def test_get_postings(self, entries, errors, _): # -> None:
        """
        option "plugin_processing_mode" "raw"

        2012-01-01 open Assets:Bank:Checking
        2012-01-01 open Expenses:Restaurant
        2012-01-01 open Expenses:Movie
        2012-01-01 open Liabilities:CreditCard
        2012-01-01 open Equity:Opening-Balances

        2012-01-15 pad Assets:Bank:Checking Equity:Opening-Balances

        2012-03-01 * "Food"
          Expenses:Restaurant     11.11 CAD
          Assets:Bank:Checking   -11.11 CAD

        2012-03-05 * "Food"
          Expenses:Movie         22.22 CAD
          Assets:Bank:Checking  -22.22 CAD

        2012-03-10 * "Paying off credit card"
          Assets:Bank:Checking     -33.33 CAD
          Liabilities:CreditCard    33.33 CAD

        2012-03-20 note Assets:Bank:Checking "Bla bla 444.44"

        2013-04-01 balance Assets:Bank:Checking   555.00 CAD

        2013-04-20 price CAD 0.91 USD

        2013-04-21 event "location" "Somewhere, USA"

        2013-04-22 custom "customentry" Assets:Bank:Checking
        2013-04-22 custom "customentry" "just a string, no account"

        2013-05-01 close Assets:Bank:Checking
        """
        ...
    
    def test_compare_realizations(self): # -> None:
        ...
    
    @loader.load_doc()
    def test_iterate_with_balance(self, entries, _, __): # -> None:
        """
        2012-01-01 open Assets:Bank:Checking
        2012-01-01 open Expenses:Restaurant
        2012-01-01 open Equity:Opening-Balances

        2012-01-15 pad Assets:Bank:Checking Equity:Opening-Balances

        2012-01-20 balance Assets:Bank:Checking  20.00 USD

        2012-03-01 * "With a single entry"
          Expenses:Restaurant     11.11 CAD
          Assets:Bank:Checking

        2012-03-02 * "With two entries"
          Expenses:Restaurant     20.01 CAD
          Expenses:Restaurant     20.02 CAD
          Assets:Bank:Checking

        2012-03-02 note Expenses:Restaurant  "This was good"

        2012-04-01 balance Expenses:Restaurant  51.14 CAD
        """
        ...
    
    def test_compute_balance(self): # -> None:
        ...
    
    @loader.load_doc()
    def test_dump(self, entries, _, __): # -> None:
        """
        2012-01-01 open Assets:Bank1:Checking
        2012-01-01 open Assets:Bank1:Savings
        2012-01-01 open Assets:Bank2:Checking
        2012-01-01 open Expenses:Restaurant
        2012-01-01 open Expenses:Movie
        2012-01-01 open Liabilities:CreditCard
        2012-01-01 open Equity:Opening-Balances
        """
        ...
    
    @loader.load_doc()
    def test_dump_balances(self, entries, _, options_map): # -> None:
        """
        2012-01-01 open Expenses:Restaurant
        2012-01-01 open Liabilities:US:CreditCard
        2012-01-01 open Liabilities:CA:CreditCard

        2014-05-30 *
          Liabilities:CA:CreditCard   123.45 CAD
          Expenses:Restaurant

        2014-05-31 *
          Liabilities:US:CreditCard   123.45 USD
          Expenses:Restaurant

        """
        ...
    


class TestRealMisc(unittest.TestCase):
    def test_index_key(self): # -> None:
        ...
    


class TestFindLastActive(unittest.TestCase):
    @loader.load_doc()
    def test_find_last_active_posting(self, entries, _, __): # -> None:
        """
        2012-01-01 open Assets:Target
        2012-01-01 open Equity:Other

        2014-02-01 *
          Assets:Target            123.45 CAD
          Equity:Other

        2014-03-01 U "This should get ignored because of the unrealized flag."
          Assets:Target            -23.45 CAD
          Equity:Other

        ;; This should get ignored because it's not one of the directives checked for
        ;; active.
        2014-03-02 event "location" "Somewhere, Somewhereland"
        """
        ...
    


class TestComputeBalance(unittest.TestCase):
    @loader.load_doc(expect_errors=True)
    def test_compute_postings_balance(self, entries, _, __): # -> None:
        """
        2014-01-01 open Assets:Bank:Checking
        2014-01-01 open Assets:Bank:Savings
        2014-01-01 open Assets:Investing
        2014-01-01 open Assets:Other

        2014-05-26 note Assets:Investing "Buying some shares"

        2014-05-30 *
          Assets:Bank:Checking  111.23 USD
          Assets:Bank:Savings   222.74 USD
          Assets:Bank:Savings   17.23 CAD
          Assets:Investing      10000 EUR
          Assets:Investing      32 HOOL {45.203 USD}
          Assets:Other          1000 EUR @ 1.78 GBP
          Assets:Other          1000 EUR @@ 1780 GBP
        """
        ...
    


if __name__ == '__main__':
    ...
