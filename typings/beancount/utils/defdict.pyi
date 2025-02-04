"""
This type stub file was generated by pyright.
"""

import collections

"""An instance of collections.defaultdict whose factory accepts a key.

Note: This really ought to be an enhancement to Python itself. I should bother
adding this in eventually.
"""
__copyright__ = ...
__license__ = ...
class DefaultDictWithKey(collections.defaultdict):
    """A version of defaultdict whose factory accepts the key as an argument.
    Note: collections.defaultdict would be improved by supporting this directly,
    this is a common occurrence.
    """
    def __missing__(self, key):
        ...
    


NOTFOUND = ...
class ImmutableDictWithDefault(dict):
    """An immutable dict which returns a default value for missing keys.

    This differs from a defaultdict in that it does not insert a missing default
    value when one is materialized (from a missing fetch), and furthermore, the
    set method is make unavailable to prevent mutation beyond construction.
    """
    def __init__(self, *args, default=...) -> None:
        ...
    
    def __setitem__(self, key, value):
        """Disallow mutating the dict in the usual way."""
        ...
    
    def __getitem__(self, key): # -> None:
        ...
    
    def get(self, key, _=...): # -> None:
        ...
    
    def __getstate__(self): # -> tuple[Any | None, list[tuple[Any, Any]]]:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    
    def __reduce__(self): # -> tuple[type[ImmutableDictWithDefault], tuple[()], tuple[Any | None, list[tuple[Any, Any]]]]:
        ...
    


