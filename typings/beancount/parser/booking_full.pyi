"""
This type stub file was generated by pyright.
"""

import enum

"""Full (new) booking implementation.

Problem description:

Interpolation and booking feed on each other, that is, numbers filled in from
interpolation might affect the booking process, and numbers derived from the
booking process may help carry out interpolation that would otherwise be
under-defined. Here's an example of interpolation helping the booking process:

Assume the ante-inventory of Assets:Investments contains two lots of shares of
HOOL, one at 100.00 USD and the other at 101.00 USD and apply this transaction:

    2015-09-30 *
      Assets:Investments   -10 HOOL {USD}
      Assets:Cash               1000 USD
      Income:Gains              -200 USD

Interpolation is unambiguously able to back out a cost of 100 USD / HOOL, which
would then result in an unambiguous booking result.

On the other hand, consider this transaction:

    2015-09-30 *
      Assets:Investments    -10 HOOL {USD}
      Assets:Cash               1000 USD
      Income:Gains

Now the interpolation cannot succeed. If the Assets:Investments account is
configured to use the FIFO method, the 10 oldest shares would be selected for
the cost, and we could then interpolate the capital gains correctly.

First observation: The second case is much more frequent than the first, and the
first is easily resolved manually by requiring a particular cost be specified.
Moreover, in many cases there isn't just a single lot of shares to be reduced
from and figuring out the correct set of shares given a target cost is an
underspecified problem.

Second observation: Booking can only be achieved for inventory reductions, not
for augmentations. Therefore, we should carry out booking on inventory
reductions and fail early if reduction is undefined there, and leave inventory
augmentations with missing numbers undefined, so that interpolation can fill
them in at a later stage.

Note that one case we'd like to but may not be able to handle is of a reduction
with interpolated price, like this:

    2015-09-30 *
      Assets:Investments        -10 HOOL {100.00 # USD}
      Expenses:Commission      9.95 USD
      Assets:Cash            990.05 USD

Therefore we choose to

1) Carry out booking first, on inventory reductions only, and leave inventory
   augmentations as they are, possibly undefined. The 'cost' attributed of
   booked postings are converted from CostSpec to Cost. Augmented postings with
   missing amounts are left as CostSpec instances in order to allow for
   interpolation of total vs. per-unit amount.

2) Compute interpolations on the resulting postings. Undefined costs for
   inventory augmentations may be filled in by interpolations at this stage (if
   possible).

3) Finally, convert the interpolated CostSpec instances to Cost instances.

Improving on this algorithm would require running a loop over the booking and
interpolation steps until all numbers are resolved or no more inference can
occur. We may consider that for later, as an experimental feature. My hunch is
that there are so few cases for which this would be useful that we won't bother
improving on the algorithm above.
"""
__copyright__ = ...
__license__ = ...
def unique_label() -> str:
    "Return a globally unique label for cost entries."
    ...

SelfReduxError = ...
def book(entries, options_map, methods): # -> tuple[list[Any], list[Any]]:
    """Interpolate missing data from the entries using the full historical algorithm.
    See the internal implementation _book() for details.
    This method only stripes some of the return values.

    See _book() for arguments and return values.
    """
    ...

CategorizationError = ...
def get_bucket_currency(refer): # -> str | None:
    """Given currency references for a posting, return the bucket currency.

    Args:
      refer: An instance of Refer.
    Returns:
      A currency string.
    """
    ...

Refer = ...
def categorize_by_currency(entry, balances):
    """Group the postings by the currency they declare.

    This is used to prepare the postings for the next stages: Interpolation and
    booking will then be carried out separately on each currency group. At the
    outset of this routine, we should have distinct groups of currencies without
    any ambiguities regarding which currency they need to balance against.

    Here's how this works.

    - First we apply the constraint that cost-currency and price-currency must
      match, if there is both a cost and a price. This reduces the space of
      possibilities somewhat.

    - If the currency is explicitly specified, we put the posting in that
      currency's bucket.

    - If not, we have a few methods left to disambiguate the currency:

      1. We look at the remaining postings... if they are all of a single
         currency, the posting must be in that currency too.

      2. If we cannot do that, we inspect the contents of the inventory of the
         account for the posting. If all the contents are of a single currency,
         we use that one.

    Args:
      postings: A list of incomplete postings to categorize.
      balances: A dict of currency to inventory contents before the transaction is
        applied.
    Returns:
      A list of (currency string, list of tuples) items describing each postings
      and its interpolated currencies, and a list of generated errors for
      currency interpolation. The entry's original postings are left unmodified.
      Each tuple in the value-list contains:
        index: The posting index in the original entry.
        units_currency: The interpolated currency for units.
        cost_currency: The interpolated currency for cost.
        price_currency: The interpolated currency for price.
    """
    ...

def replace_currencies(postings, refer_groups): # -> list[Any]:
    """Replace resolved currencies in the entry's Postings.

    This essentially applies the findings of categorize_by_currency() to produce
    new postings with all currencies resolved.

    Args:
      postings: A list of Posting instances to replace.
      refer_groups: A list of (currency, list of posting references) items as
        returned by categorize_by_currency().
    Returns:
      A new list of items of (currency, list of Postings), postings for which the
      currencies have been replaced by their interpolated currency values.
    """
    ...

ReductionError = ...
def has_self_reduction(postings, methods): # -> bool:
    """Return true if the postings potentially reduce each other at cost.

    Args:
      postings: A list of postings with uninterpolated CostSpec cost instances.
      methods: A mapping of account name to their corresponding booking
        method.
    Returns:
      A boolean, true if there's a potential for self-reduction.
    """
    ...

def book_reductions(entry, group_postings, balances, methods): # -> tuple[list[Any], list[Any]]:
    """Book inventory reductions against the ante-balances.

    This function accepts a dict of (account, Inventory balance) and for each
    posting that is a reduction against its inventory, attempts to find a
    corresponding lot or list of lots to reduce the balance with.

    * For reducing lots, the CostSpec instance of the posting is replaced by a
      Cost instance.

    * For augmenting lots, the CostSpec instance of the posting is left alone,
      except for its date, which is inherited from the parent Transaction.

    Args:
      entry: An instance of Transaction. This is only used to refer to when
        logging errors.
      group_postings: A list of Posting instances for the group.
      balances: A dict of account name to inventory contents.
      methods: A mapping of account name to their corresponding booking
        method enum.
    Returns:
      A pair of
        booked_postings: A list of booked postings, with reducing lots resolved
          against specific position in the corresponding accounts'
          ante-inventory balances. Note single reducing posting in the input may
          result in multiple postings in the output. Also note that augmenting
          postings held-at-cost will still refer to 'cost' instances of
          CostSpec, left to be interpolated later.
        errors: A list of errors, if there were any.
    """
    ...

def compute_cost_number(costspec, units): # -> None:
    """Given a CostSpec, return the cost number, if possible to compute.

    Args:
      costspec: A parsed instance of CostSpec.
      units: An instance of Amount for the units of the position.
    Returns:
      If it is not possible to calculate the cost, return None.
      Otherwise, returns a Decimal instance, the per-unit cost.
    """
    ...

def convert_costspec_to_cost(posting):
    """Convert an instance of CostSpec to Cost, if present on the posting.

    If the posting has no cost, it itself is just returned.

    Args:
      posting: An instance of Posting.
    Returns:
      An instance of Posting with a possibly replaced 'cost' attribute.
    """
    ...

class MissingType(enum.Enum):
    """The type of missing number."""
    UNITS = ...
    COST_PER = ...
    COST_TOTAL = ...
    PRICE = ...


InterpolationError = ...
def interpolate_group(postings, balances, currency, tolerances):
    """Interpolate missing numbers in the set of postings.

    Args:
      postings: A list of Posting instances.
      balances: A dict of account to its ante-inventory.
      currency: The weight currency of this group, used for reporting errors.
      tolerances: A dict of currency to tolerance values.
    Returns:
      A tuple of
        postings: A lit of new posting instances.
        errors: A list of errors generated during interpolation.
        interpolated: A boolean, true if we did have to interpolate.

      In the case of an error, this returns the original list of postings, which
      is still incomplete. If an error is returned, you should probably skip the
      transaction altogether, or just not include the postings in it. (An
      alternative behaviour would be to return only the list of valid postings,
      but that would likely result in an unbalanced transaction. We do it this
      way by choice.)
    """
    ...

