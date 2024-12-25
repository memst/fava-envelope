"""
This type stub file was generated by pyright.
"""

"""Execution of interpreter on data rows.
"""
__copyright__ = ...
__license__ = ...
def uniquify(iterable): # -> Generator[Any, Any, None]:
    ...

def execute_print(c_print, file): # -> None:
    """Print entries from a print statement specification.

    Args:
      c_print: An instance of a compiled EvalPrint statement.
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
    


class NullType:
    """An object that compares smaller than anything.

    An instance of this class is used to replace None in BQL query
    results in sort keys to obtain sorting semantics similar to SQL
    where NULL is sortet at the beginning.

    """
    __slots__ = ...
    def __repr__(self): # -> Literal['NULL']:
        ...
    
    __str__ = ...
    def __lt__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    


NULL = ...
def nullitemgetter(item, *items): # -> Callable[..., tuple[Any, ...]]:
    """An itemgetter() that replaces None values with NULL."""
    ...

def execute_query(query): # -> tuple[tuple[Column, ...], list[tuple[Any, ...]]] | tuple[tuple[Column, ...], list[Any]]:
    """Given a compiled select statement, execute the query.

    Args:
      query: The query to execute.
      entries: A list of directives.
      options: A parser's option_map.

    Returns:
        A list of (name, dtype) tuples describing the results set
        table and a list of ResultRow tuples with the data.item pairs.

    """
    ...

def execute_select(query): # -> tuple[tuple[Column, ...], list[tuple[Any, ...]]]:
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

