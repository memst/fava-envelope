"""
This type stub file was generated by pyright.
"""

import datetime
from decimal import Decimal
from typing import Optional, Set

from beancount.core.data import Currency

"""This module has code that can build a database of historical prices at
various times, from which unrealized capital gains and market value can be
deduced.

Prices are deduced from Price entries found in the file, or perhaps
created by scripts (for example you could build a script that will fetch
live prices online and create entries on-the-fly).
"""
__copyright__ = ...
__license__ = ...

def get_last_price_entries(entries, date):  # -> list[Any]:
    """Run through the entries until the given date and return the last
    Price entry encountered for each (currency, cost-currency) pair.

    Args:
      entries: A list of directives.
      date: An instance of datetime.date. If None, the very latest price
        is returned.
    Returns:
      A list of price entries.
    """
    ...

class PriceMap(dict):
    """A price map dictionary.

    The keys include both the set of forward (base, quote) pairs and their
    inverse. In order to determine which are the forward pairs, access the
    'forward_pairs' attribute

    Attributes:
      forward_pairs: A list of (base, quote) keys for the forward pairs.
    """

    __slots__ = ...

def build_price_map(entries) -> PriceMap:
    """Build a price map from a list of arbitrary entries.

    If multiple prices are found for the same (currency, cost-currency) pair at
    the same date, the latest date is kept and the earlier ones (for that day)
    are discarded.

    If inverse price pairs are found, e.g. USD in AUD and AUD in USD, the
    inverse that has the smallest number of price points is converted into the
    one that has the most price points. In that way they are reconciled into a
    single one.

    Args:
      entries: A list of directives, hopefully including some Price and/or
      Transaction entries.
    Returns:
      A dict of (currency, cost-currency) keys to sorted lists of (date, number)
      pairs, where 'date' is the date the price occurs at and 'number' a Decimal
      that represents the price, or rate, between these two
      currencies/commodities. Each date occurs only once in the sorted list of
      prices of a particular key. All of the inverses are automatically
      generated in the price map.
    """
    ...

def project(
    orig_price_map: PriceMap,
    from_currency: Currency,
    to_currency: Currency,
    base_currencies: Optional[Set[Currency]] = ...,
) -> PriceMap:
    """Project all prices with a quote currency to another quote currency.

    Say you have a price for HOOL in USD and you'd like to convert HOOL to CAD.
    If there aren't any (HOOL, CAD) price pairs in the database it will remain
    unconverted. Projecting from USD to CAD will compute combined rates and
    insert corresponding prices over all base currencies (like HOOL). In this
    example, each of the (HOOL, USD) prices would see an inserted (HOOL, CAD)
    price inserted at the same date.

    It is common to make these projections when reducing inventories in a ledger
    that states multiple operating currency pairs, when for example, one wants
    to compute total value of a set of accounts in one of those currencies.

    Please note that:

    - Even if the target pair has existing entries, projection will still be
      applied. For example, is there exist some (HOOL, CAD) prices, the
      projection in the example above will still insert some new price points to
      it.

    - However, projected prices colliding existing ones at the same date will
      not override them.

    - Projection will fail to insert a new price if the conversion between to
      and from currencies has no existing prices (e.g. before its first price
      entry).

    - Perhaps most importantly, we only insert price points at dates where the
      base commodity has a price point. In other words, if we have prices for
      dates A and C and the rate changes between these dates at date B, we don't
      synthesize a new price at date B. A more accurate method to get projected
      prices that takes into account varying rates is to do multiple lookups.
      We'll eventually add a method to query it via a specified list of
      intermediate pairs. {c1bd24f8d4b7}

    Args:
      orig_price_map: An existing price map.
      from_currency: The quote currency with existing project points (e.g., USD).
      to_currency: The quote currency to insert price points for (e.g., CAD).
      base_currencies: An optional set of commodities to restrict the
        projections to (e.g., {HOOL}).
    Returns:
      A new price map, with the extra projected prices. The original price map
      is kept intact.
    """
    ...

def normalize_base_quote(base_quote):  # -> tuple[str, str] | tuple[Any, ...]:
    """Convert a slash-separated string to a pair of strings.

    Args:
      base_quote: A pair of strings, the base currency to lookup, and the quote
        currency to lookup, which expresses which units the base currency is
        denominated in. This may also just be a string, with a '/' separator.
    Returns:
      A pair of strings.
    """
    ...

def get_all_prices(price_map, base_quote):
    """Return a sorted list of all (date, number) price pairs.

    Args:
      price_map: A price map, which is a dict of (base, quote) -> list of (date,
        number) tuples, as created by build_price_map.
      base_quote: A pair of strings, the base currency to lookup, and the quote
        currency to lookup, which expresses which units the base currency is
        denominated in. This may also just be a string, with a '/' separator.
    Returns:
      A list of (date, Decimal) pairs, sorted by date.
    Raises:
      KeyError: If the base/quote could not be found.
    """
    ...

def get_latest_price(
    price_map, base_quote
):  # -> tuple[None, Decimal] | tuple[None, None]:
    """Return the latest price/rate from a price map for the given base/quote pair.
    This is often used to just get the 'current' price if you're looking at the
    entire set of entries.

    Args:
      price_map: A price map, which is a dict of (base, quote) -> list of (date,
        number) tuples, as created by build_price_map.
    Returns:
      A pair of (date, number), where 'date' is a datetime.date instance and
      'number' is a Decimal of the price, or rate, at that date. The date is the
      latest date which we have an available price for in the price map.
    """
    ...

def get_price(
    price_map: PriceMap, base_quote: tuple[str, str], date: datetime.date
) -> tuple[datetime.date, Decimal] | tuple[None, None]:
    """Return the price as of the given date.

    If the date is unspecified, return the latest price.

    Args:
      price_map: A price map, which is a dict of (base, quote) -> list of (date,
        number) tuples, as created by build_price_map.
      base_quote: A pair of strings, the base currency to lookup, and the quote
        currency to lookup, which expresses which units the base currency is
        denominated in. This may also just be a string, with a '/' separator.
      date: A datetime.date instance, the date at which we want the conversion
        rate.
    Returns:
      A pair of (datetime.date, Decimal) instance. If no price information could
      be found, return (None, None).
    """
    ...
