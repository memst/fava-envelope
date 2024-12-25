"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
__copyright__ = ...
__license__ = ...
ZERO = ...
HALF = ...
ONE = ...
class MISSING:
    ...


NUMBER_RE = ...
_CLEAN_NUMBER_RE = ...
def D(strord=...):
    """Convert a string into a Decimal object.

    This is used in parsing amounts from files in the importers. This is the
    main function you should use to build all numbers the system manipulates
    (never use floating-point in an accounting system). Commas are stripped and
    ignored, as they are assumed to be thousands separators (the French comma
    separator as decimal is not supported). This function just returns the
    argument if it is already a Decimal object, for convenience.

    Args:
      strord: A string or Decimal instance.
    Returns:
      A Decimal instance.
    """
    ...

def round_to(number, increment):
    """Round a number *down* to a particular increment.

    Args:
      number: A Decimal, the number to be rounded.
      increment: A Decimal, the size of the increment.
    Returns:
      A Decimal, the rounded number.
    """
    ...

def same_sign(number1, number2):
    """Return true if both numbers have the same sign.

    Args:
      number1: An instance of Decimal.
      number2: An instance of Decimal.
    Returns:
      A boolean.
    """
    ...

