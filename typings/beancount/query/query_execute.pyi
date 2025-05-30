"""
This type stub file was generated by pyright.
"""

"""Execution of interpreter on data rows.
"""
__copyright__ = ...
__license__ = ...
def filter_entries(c_from, entries, options_map, context): # -> list[Any]:
    """Filter the entries by the given compiled FROM clause.

    Args:
      c_from: A compiled From clause instance.
      entries: A list of directives.
      options_map: A parser's option_map.
      context: A prototype of RowContext to use for evaluation.
    Returns:
      A list of filtered entries.
    """
    ...

def execute_print(c_print, entries, options_map, file): # -> None:
    """Print entries from a print statement specification.

    Args:
      c_print: An instance of a compiled EvalPrint statement.
      entries: A list of directives.
      options_map: A parser's option_map.
      file: The output file to print to.
    """
    ...

class Allocator:
    """A helper class to count slot allocations and return unique handles to them.
    """
    def __init__(self) -> None:
        ...
    
    def allocate(self): # -> int:
        """Allocate a new slot to store row aggregation information.

        Returns:
          A unique handle used to index into an row-aggregation store (an integer).
        """
        ...
    
    def create_store(self): # -> list[None]:
        """Create a new row-aggregation store suitable to contain all the node allocations.

        Returns:
          A store that can accommodate and be indexed by all the allocated slot handles.
        """
        ...
    


class RowContext:
    """A dumb container for information used by a row expression."""
    posting = ...
    entry = ...
    balance = ...
    options_map = ...
    account_types = ...
    open_close_map = ...
    commodity_map = ...
    price_map = ...


def uses_balance_column(c_expr): # -> bool:
    """Return true if the expression accesses the special 'balance' column.

    Args:
      c_expr: A compiled expression tree (an EvalNode node).
    Returns:
      A boolean, true if the expression contains a BalanceColumn node.
    """
    ...

_MIN_VALUES = ...
def row_sortkey(order_indexes, values, c_exprs): # -> tuple[Any, ...] | None:
    """Generate a sortkey for the given values.

    Args:
      order_indexes: The indexes by which the rows should be sorted.
      values: The computed values in the row.
      c_exprs: The matching c_expr's.
    Returns:
      A tuple, the sortkey.
    """
    ...

def create_row_context(entries, options_map): # -> RowContext:
    """Create the context container which we will use to evaluate rows."""
    ...

def execute_query(query, entries, options_map):
    """Given a compiled select statement, execute the query.

    Args:
      query: An instance of a query_compile.Query
      entries: A list of directives.
      options_map: A parser's option_map.
    Returns:
      A pair of:
        result_types: A list of (name, data-type) item pairs.
        result_rows: A list of ResultRow tuples of length and types described by
          'result_types'.
    """
    ...

def flatten_results(result_types, result_rows): # -> tuple[Any, Any] | tuple[list[tuple[Any, type[Position] | Any]], list[Any]]:
    """Convert inventories in result types to have a row for each.

    This routine will expand all result lines with an inventory into a new line
    for each position.

    Args:
        result_types: A list of (name, data-type) item pairs.
        result_rows: A list of ResultRow tuples of length and types described by
          'result_types'.
    Returns:
        result_types: A list of (name, data-type) item pairs. There should be no
          Inventory types anymore.
        result_rows: A list of ResultRow tuples of length and types described by
          'result_types'. All inventories from the input should have been converted
          to Position types.
    """
    ...

