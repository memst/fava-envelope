"""
This type stub file was generated by pyright.
"""

import unittest
from beancount.parser import parser

"""
Test various options.
"""
__copyright__ = ...
__license__ = ...
class TestOptions(unittest.TestCase):
    def test_get_account_types(self): # -> None:
        ...
    
    def test_get_previous_accounts(self): # -> None:
        ...
    
    def test_get_current_accounts(self): # -> None:
        ...
    
    def test_list_options(self): # -> None:
        ...
    


class TestAccountTypeOptions(unittest.TestCase):
    @parser.parse_doc()
    def test_custom_account_names__success(self, entries, errors, options_map): # -> None:
        """
          option "name_assets" "Actif"
          option "name_liabilities" "Passif"
          option "name_equity" "Capital"
          option "name_income" "Revenu"
          option "name_expenses" "Dépenses"

          2014-01-04 open Actif:CA:RBC:CompteChèques
          2014-01-04 open Passif:CA:RBC:CarteDeCrédit
          2014-01-04 open Capital:Ouverture
          2014-01-04 open Revenu:Salaire
          2014-01-04 open Dépenses:Bistrot
        """
        ...
    
    @parser.parse_doc()
    def test_custom_account_names__success_reset(self, entries, errors, options_map): # -> None:
        """
          2014-01-01 open Assets:CA:RBC:Checking

          option "name_assets" "Actif"

          2014-01-04 open Actif:CA:RBC:CompteChèques
        """
        ...
    
    @parser.parse_doc(expect_errors=True)
    def test_custom_account_names__basic_fail(self, entries, errors, options_map): # -> None:
        """
          2014-01-04 open Actif:CA:RBC:CompteChèques
          2014-01-04 open Passif:CA:RBC:CarteDeCrédit
        """
        ...
    
    @parser.parse_doc(expect_errors=True)
    def test_custom_account_names__fail_invalid_order(self, entries, errors, options_map): # -> None:
        """
          2014-01-04 open Actif:CA:RBC:CompteChèques

          option "name_assets" "Actif"
        """
        ...
    
    @parser.parse_doc(expect_errors=True)
    def test_custom_account_names__fail_invalid_other(self, entries, errors, options_map): # -> None:
        """
          2014-01-01 open Assets:CA:RBC:Checking

          option "name_assets" "Actif"

          2014-01-04 open Assets:CA:RBC:Checking
        """
        ...
    


class TestValidateOptions(unittest.TestCase):
    @parser.parse_doc(expect_errors=True)
    def test_validate__plugin_processing_mode__invalid(self, entries, errors, options_map): # -> None:
        """
          option "plugin_processing_mode" "i-dont-exist"
        """
        ...
    


if __name__ == '__main__':
    ...
