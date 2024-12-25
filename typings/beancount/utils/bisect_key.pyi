"""
This type stub file was generated by pyright.
"""

"""A version of bisect that accepts a custom key function, like the sorting ones do.
"""
__copyright__ = ...
__license__ = ...
def bisect_left_with_key(sequence, value, key=...): # -> int:
    """Find the last element before the given value in a sorted list.

    Args:
      sequence: A sorted sequence of elements.
      value: The value to search for.
      key: An optional function used to extract the value from the elements of
        sequence.
    Returns:
      Return the index. May return None.
    """
    ...

def bisect_right_with_key(a, x, key, lo=..., hi=...): # -> int:
    """Like bisect.bisect_right, but with a key lookup parameter.

    Args:
      a: The list to search in.
      x: The element to search for.
      key: A function, to extract the value from the list.
      lo: The smallest index to search.
      hi: The largest index to search.
    Returns:
      As in bisect.bisect_right, an element from list 'a'.
    """
    ...

