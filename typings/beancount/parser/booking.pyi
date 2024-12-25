"""
This type stub file was generated by pyright.
"""

"""Algorithms for 'booking' inventory, that is, the process of finding a
matching lot when reducing the content of an inventory.
"""
__copyright__ = ...
__license__ = ...
BookingError = ...
def book(incomplete_entries, options_map): # -> tuple[list[Any], list[Any]]:
    """Book inventory lots and complete all positions with incomplete numbers.

    Args:
      incomplete_entries: A list of directives, with some postings possibly left
        with incomplete amounts as produced by the parser.
      options_map: An options dict as produced by the parser.
    Returns:
      A pair of
        entries: A list of completed entries with all their postings completed.
        errors: New errors produced during interpolation.
    """
    ...

def validate_missing_eliminated(entries, unused_options_map): # -> list[Any]:
    """Validate that all the missing bits of postings have been eliminated.

    Args:
      entries: A list of directives.
      unused_options_map: An options map.
    Returns:
      A list of errors.
    """
    ...

def validate_inventory_booking(entries, unused_options_map, booking_methods): # -> list[Any]:
    """Validate that no position at cost is allowed to go negative.

    This routine checks that when a posting reduces a position, existing or not,
    that the subsequent inventory does not result in a position with a negative
    number of units. A negative number of units would only be required for short
    trades of trading spreads on futures, and right now this is not supported.
    It would not be difficult to support this, however, but we want to be strict
    about it, because being pedantic about this is otherwise a great way to
    detect user data entry mistakes.

    Args:
      entries: A list of directives.
      unused_options_map: An options map.
      booking_methods: A mapping of account name to booking method, accumulated
        in the main loop.
    Returns:
      A list of errors.

    """
    ...

def convert_lot_specs_to_lots(entries): # -> tuple[list[Any], list[Any]]:
    """For all the entries, convert the posting's position's CostSpec to Cost
    instances. In the simple method, the data provided in the CostSpec must
    unambiguously provide a way to compute the cost amount.

    This essentially replicates the way the old parser used to work, but
    allowing positions to have the fuzzy lot specifications instead of the
    resolved ones. We used to simply compute the costs locally, and this gets
    rid of the CostSpec to produce the Cost without fuzzy matching. This is only
    there for the sake of transition to the new matching logic.

    Args:
      entries: A list of incomplete directives as per the parser.
    Returns:
      A list of entries whose postings's position costs have been converted to
      Cost instances but that may still be incomplete.
    Raises:
      ValueError: If there's a unacceptable number.
    """
    ...

def convert_spec_to_cost(units, cost_spec): # -> Cost | None:
    """Convert a posting's CostSpec instance to a Cost.

    Args:
      units: An instance of Amount.
      cost_spec: An instance of CostSpec.
    Returns:
      An instance of Cost.
    """
    ...

