"""
This type stub file was generated by pyright.
"""

"""A simple accumulator for data about a mathematical distribution.
"""
__copyright__ = ...
__license__ = ...
class Distribution:
    """A class that computes a histogram of integer values. This is used to compute
    a length that will cover at least some decent fraction of the samples.
    """
    def __init__(self) -> None:
        ...
    
    def empty(self): # -> bool:
        """Return true if the distribution is empty.

        Returns:
          A boolean.
        """
        ...
    
    def update(self, value): # -> None:
        """Add a sample to the distribution.

        Args:
          value: A value of the function.
        """
        ...
    
    def update_from(self, other): # -> None:
        """Add samples from the other distribution to this one.

        Args:
          other: Another distribution.
        """
        ...
    
    def min(self): # -> None:
        """Return the minimum value seen in the distribution.

        Returns:
          An element of the value type, or None, if the distribution was empty.
        """
        ...
    
    def max(self): # -> None:
        """Return the minimum value seen in the distribution.

        Returns:
          An element of the value type, or None, if the distribution was empty.
        """
        ...
    
    def mode(self): # -> Literal[0] | None:
        """Return the mode of the distribution.

        Returns:
          An element of the value type, or None, if the distribution was empty.
        """
        ...
    


