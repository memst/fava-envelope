from dataclasses import dataclass, field

from beancount.core.inventory import Inventory


@dataclass
class Income:
    avail_income: Inventory = field(default_factory=Inventory)
    rolled_over: Inventory = field(default_factory=Inventory)
    budgeted: Inventory = field(default_factory=Inventory)
    to_be_budgeted: Inventory = field(default_factory=Inventory)


@dataclass
class Envelope:
    allocate_fill: bool = field(default=False)
    budgeted: Inventory = field(default_factory=Inventory)

    activity: Inventory = field(default_factory=Inventory)
    available: Inventory = field(default_factory=Inventory)
