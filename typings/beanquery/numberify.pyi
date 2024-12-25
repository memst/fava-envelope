"""
This type stub file was generated by pyright.
"""

from decimal import Decimal

"""Code to split table columns containing amounts and inventories into number columns.

For example, given a column with this content:

    ----- amount ------
    101.23 USD
       200 JPY
     99.23 USD
     38.34 USD, 100 JPY

We can convert this into two columns and remove the currencies:

    -amount (USD)- -amount (JPY)-
            101.23
                              200
             99.23
             38.34            100

The point is that the columns should be typed as numbers to make this importable
into a spreadsheet and able to be processed.

Notes:

* This handles the Amount, Position and Inventory datatypes. There is code to
  automatically recognize columns containing such types from a table of strings
  and convert such columns to their corresponding guessed data types.

* The per-currency columns are ordered in decreasing order of the number of
  instances of numbers seen for each currency. So if the most numbers you have
  in a column are USD, then the USD column renders first.

* Cost basis specifications should be unmodified and reported to a dedicated
  extra column, like this:

    ----- amount ------
    1 AAPL {21.23 USD}

  We can convert this into two columns and remove the currencies:

    -amount (AAPL)- -Cost basis-
                  1 {21.23 USD}

  (Eventually we might support the conversion of cost amounts as well, but they
  may contain other information, such as a label or a date, so for now we don't
  convert them. I'm not sure there's a good practical use case in doing that
  yet.)

* We may provide some options to break out only some of the currencies into
  columns, in order to handle the case where an inventory contains a large
  number of currencies and we want to only operate on a restricted set of
  operating currencies.

* If you provide a DisplayFormatter object to the numberification routine, they
  quantize each column according to their currency's precision. It is
  recommended that you do that.

"""
__copyright__ = ...
__license__ = ...
def numberify_results(columns, drows, dformat=...): # -> tuple[tuple[Column, ...], list[Any]]:
    """Number rows containing Amount, Position or Inventory types.

    Args:
      result_types: A list of items describing the names and data types of the items in
        each column.
      result_rows: A list of ResultRow instances.
      dformat: An optional DisplayFormatter. If set, quantize the numbers by
        their currency-specific precision when converting the Amount's,
        Position's or Inventory'es..
    Returns:
      A pair of modified (result_types, result_rows) with converted datatypes.
    """
    ...

class IdentityConverter:
    """A converter that simply copies its column."""
    def __init__(self, name, dtype, index) -> None:
        ...
    
    def __call__(self, drow, _):
        ...
    


class AmountConverter:
    """A converter that extracts the number of an amount for a specific currency."""
    dtype = Decimal
    def __init__(self, name, index, currency) -> None:
        ...
    
    def __call__(self, drow, dformat): # -> None:
        ...
    


def convert_col_Amount(name, drows, index): # -> list[AmountConverter]:
    """Create converters for a column of type Amount.

    Args:
      name: A string, the column name.
      drows: The table of objects.
      index: The column number.
    Returns:
      A list of Converter instances, one for each of the currency types found.
    """
    ...

class PositionConverter:
    """A converter that extracts the number of a position for a specific currency."""
    dtype = Decimal
    def __init__(self, name, index, currency) -> None:
        ...
    
    def __call__(self, drow, dformat): # -> None:
        ...
    


def convert_col_Position(name, drows, index): # -> list[PositionConverter]:
    """Create converters for a column of type Position.

    Args:
      name: A string, the column name.
      drows: The table of objects.
      index: The column number.
    Returns:
      A list of Converter instances, one for each of the currency types found.
    """
    ...

class InventoryConverter:
    """A converter that extracts the number of a inventory for a specific currency.
    If there are multiple lots we aggregate by currency."""
    dtype = Decimal
    def __init__(self, name, index, currency) -> None:
        ...
    
    def __call__(self, drow, dformat): # -> None:
        ...
    


def convert_col_Inventory(name, drows, index): # -> list[InventoryConverter]:
    """Create converters for a column of type Inventory.

    Args:
      name: A string, the column name.
      drows: The table of objects.
      index: The column number.
    Returns:
      A list of Converter instances, one for each of the currency types found.
    """
    ...

CONVERTING_TYPES = ...
