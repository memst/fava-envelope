import datetime

from beancount.core import convert, prices
from beancount.core.amount import Amount
from beancount.core.data import Posting
from beancount.core.inventory import Inventory
from beancount.core.position import Position


def convert_to_operating_currency(
    pos: Position | Posting,
    price_map: prices.PriceMap,
    operating_currencies: list[str],
    date: datetime.date,
):
    """Convert a position or posting to the first available operating currency.

    Args:
      pos: An instance of Position or Posting.
      price_map:
      operating_currencies:
      date: The date to use for finding an appropriate price.
    Returns:
      An instance of Position.
    """
    if pos.units.currency in operating_currencies:
        return pos.units

    if pos.units.number is None:
        return pos.units

    convert.convert_position
    for value_currency in operating_currencies:
        base_quote = (pos.units.currency, value_currency)
        price_date, price_number = prices.get_price(price_map, base_quote, date)
        if price_number is not None:
            return Amount(pos.units.number * price_number, value_currency)

    return pos.units


def reduce_mixed_positions(
    inventory: Inventory,
    price_map: prices.PriceMap,
    operating_currency: list[str],
    date: datetime.date,
) -> Inventory:
    """
    If the inventory has a mixture of positive and negative positions, convert it
    to the primary operating currency. If some position could not be converted,
    keep it unmodified.

    Ignores and removed cost basis from inventories.
    """

    if len(inventory) < 2:
        return inventory

    is_mixed = False
    prev_sign = None
    for position in inventory:
        assert position.units.number is not None
        sign = position.units.number >= 0
        if prev_sign and prev_sign != sign:
            is_mixed = True
            break
        prev_sign = sign

    if not is_mixed:
        return inventory

    reduced_inventory = Inventory()
    for position in inventory:
        reduced_inventory.add_amount(
            convert.convert_position(position, operating_currency[0], price_map, date)
        )

    return reduced_inventory


def is_positive_inventory(inventory: Inventory) -> bool:
    "Return whether the inventory only contains positive positions."
    for pos in inventory:
        if pos.units.number is not None and pos.units.number < 0:
            return False
    return True
