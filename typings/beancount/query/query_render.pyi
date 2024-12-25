"""
This type stub file was generated by pyright.
"""

import datetime
from decimal import Decimal
from beancount.core import amount, inventory, position

"""Rendering of rows.
"""
__copyright__ = ...
__license__ = ...
class ColumnRenderer:
    """Base class for classes that render and compute formatting and width for all
    values that appear within a column. All the values rendered are assumed to
    be of the same type, or None (empty). The class receives all the values that
    will be rendered to accumulate the dimensions it will need to format them
    later on. It is then responsible to render those values in a way that will
    align nicely in a column, in the rendered output, whereby all the values
    render to the same width.
    """
    dtype = ...
    def __init__(self, unused_dcontext) -> None:
        ...
    
    def update(self, value):
        """Update the rendered with the given value.
        Args:
          value: Any object of the type 'dtype'.
        Returns:
          An integer, the number of lines this will get rendered to.
        """
        ...
    
    def prepare(self): # -> None:
        """Prepare to render all values of a column.
        This is called after having seen all the values in calls to update().
        """
        ...
    
    def width(self):
        """Return the computed width of this column.
        Returns:
          An integer, the number of characters wide required for this field.
        """
        ...
    
    def format(self, value):
        """Format the value.

        Args:
          value: Any object of the type 'dtype'.
        Returns:
          A string, or a list of strings, the rendered and aligned string(s)
          representations of for the value. A value may render on multiple
          lines, which is why a list may be returned here.
        """
        ...
    


class ObjectRenderer(ColumnRenderer):
    """A renderer for a generic object type."""
    dtype = object
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, string): # -> None:
        ...
    
    def prepare(self): # -> None:
        ...
    
    def width(self): # -> int:
        ...
    
    def format(self, string): # -> str:
        ...
    


class BoolRenderer(ColumnRenderer):
    """A renderer for left-aligned strings."""
    dtype = bool
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, value): # -> None:
        ...
    
    def prepare(self): # -> None:
        ...
    
    def width(self): # -> int:
        ...
    
    def format(self, value): # -> str:
        ...
    


class StringRenderer(ColumnRenderer):
    """A renderer for left-aligned strings."""
    dtype = str
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, string): # -> None:
        ...
    
    def prepare(self): # -> None:
        ...
    
    def width(self): # -> int:
        ...
    
    def format(self, string): # -> str:
        ...
    


class StringSetRenderer(ColumnRenderer):
    """A renderer for sets of strings."""
    dtype = set
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, string_set): # -> None:
        ...
    
    def prepare(self): # -> None:
        ...
    
    def width(self): # -> int:
        ...
    
    def format(self, string_set): # -> str | list[str]:
        ...
    


class DateTimeRenderer(ColumnRenderer):
    """A renderer for decimal numbers."""
    dtype = datetime.date
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, _): # -> None:
        ...
    
    def width(self): # -> Literal[10]:
        ...
    
    def format(self, dtime): # -> str:
        ...
    


class IntegerRenderer(ColumnRenderer):
    """A renderer for integers."""
    dtype = int
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, number): # -> None:
        ...
    
    def prepare(self): # -> None:
        ...
    
    def width(self): # -> int:
        ...
    
    def format(self, number): # -> str:
        ...
    


class DecimalRenderer(ColumnRenderer):
    """A renderer for decimal numbers."""
    dtype = Decimal
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, number, key=...): # -> None:
        ...
    
    def prepare(self): # -> None:
        ...
    
    def width(self): # -> int | None:
        ...
    
    def format(self, number, key=...): # -> str:
        ...
    


class AmountRenderer(ColumnRenderer):
    """A renderer for amounts. The currencies align with each other.
    """
    dtype = amount.Amount
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, amount_): # -> None:
        ...
    
    def prepare(self): # -> None:
        ...
    
    def width(self): # -> int:
        ...
    
    def format(self, amount_): # -> str:
        ...
    


class PositionRenderer(ColumnRenderer):
    """A renderer for positions. Inventories renders as a list of position
    strings. Both the unit numbers and the cost numbers are aligned, if any.
    """
    dtype = position.Position
    def __init__(self, dcontext) -> None:
        ...
    
    def update(self, pos): # -> None:
        ...
    
    def prepare(self): # -> None:
        ...
    
    def width(self): # -> int:
        ...
    
    def format(self, pos): # -> str | list[Any]:
        ...
    


class InventoryRenderer(PositionRenderer):
    """A renderer for Inventory instances. Inventories renders as a list of position
    strings. Both the unit numbers and the cost numbers are aligned, if any.
    """
    dtype = inventory.Inventory
    def update(self, inv): # -> None:
        ...
    
    def format(self, inv): # -> str | list[Any]:
        ...
    


def get_renderers(result_types, result_rows, dcontext): # -> list[Any]:
    """Create renderers for each column and prepare them with the given data.

    Args:
      result_types: A list of items describing the names and data types of the items in
        each column.
      result_rows: A list of ResultRow instances.
      dcontext: A DisplayContext object prepared for rendering numbers.
    Returns:
      A list of subclass instances of ColumnRenderer.
    """
    ...

def render_rows(result_types, result_rows, dcontext, expand=..., spaced=...): # -> tuple[list[Any], list[Any]]:
    """Render the result of executing a query in text format.

    Args:
      result_types: A list of items describing the names and data types of the items in
        each column.
      result_rows: A list of ResultRow instances.
      dcontext: A DisplayContext object prepared for rendering numbers.
      expand: A boolean, if true, expand columns that render to lists on multiple rows.
      spaced: If true, leave an empty line between each of the rows. This is useful if the
        results have a lot of rows that render over multiple lines.
    """
    ...

def render_text(result_types, result_rows, dcontext, file, expand=..., boxed=..., spaced=...): # -> None:
    """Render the result of executing a query in text format.

    Args:
      result_types: A list of items describing the names and data types of the items in
        each column.
      result_rows: A list of ResultRow instances.
      dcontext: A DisplayContext object prepared for rendering numbers.
      file: A file object to render the results to.
      expand: A boolean, if true, expand columns that render to lists on multiple rows.
      boxed: A boolean, true if we should render the results in a fancy-looking ASCII box.
      spaced: If true, leave an empty line between each of the rows. This is useful if the
        results have a lot of rows that render over multiple lines.
    """
    ...

def render_csv(result_types, result_rows, dcontext, file, expand=...): # -> None:
    """Render the result of executing a query in text format.

    Args:
      result_types: A list of items describing the names and data types of the items in
        each column.
      result_rows: A list of ResultRow instances.
      dcontext: A DisplayContext object prepared for rendering numbers.
      file: A file object to render the results to.
      expand: A boolean, if true, expand columns that render to lists on multiple rows.
    """
    ...

RENDERERS = ...
