from collections import defaultdict

from beancount.core import prices
from beancount.core.data import Account
from beancount.core.inventory import Inventory
from fava.context import g
from fava.ext import FavaExtensionBase

from fava_envelope.modules import convert
from fava_envelope.modules.beancount_envelope import BeancountEnvelope
from fava_envelope.modules.budgets import Envelope, Income
from fava_envelope.modules.envelope_link import EnvelopeLink
from fava_envelope.modules.year_month import YearMonth, YearMonthStr


class EnvelopeBudget(FavaExtensionBase):
    """The class handling the display of budgets in Fava."""

    # Stores whether the up-to-date version of the budget repors has been
    # cached.
    ran_budget_df: bool

    income_tables: defaultdict[YearMonth, Income]
    envelope_tables: defaultdict[Account, defaultdict[YearMonth, Envelope]]
    primary_currency: str
    price_map: prices.PriceMap

    available_months: list[YearMonth]
    available_months_str: list[YearMonthStr]

    report_title = "Envelope Budget"

    def after_delete_entry(self, entry):
        self.reset_cache()

    def after_entry_modified(self, entry, new_lines):
        self.reset_cache()

    def after_insert_entry(self, entry):
        self.reset_cache()

    def after_insert_metadata(self, entry, key, value):
        self.reset_cache()

    def after_load_file(self):
        self.reset_cache()

    def after_write_source(self, path, source):
        self.reset_cache()

    def reset_cache(self):
        self.ran_budget_df = False

    def generate_budget_df(self, currency):
        if self.ran_budget_df:
            return

        module = BeancountEnvelope(
            g.ledger.all_entries,
            self.ledger.options,
            currency,
            g.ledger.errors,
        )
        # TODO memst: I don't like how this code is structured and BeancountEnvelope
        # should have a better interface. The evnvelope_tables is computed only once per
        # instance anyway (argumentless function), so it should be completely fine to make
        # the whole thing a dataclass or something similar where you can just access some
        # values after creation.
        (self.income_tables, self.envelope_tables, _) = module.envelope_tables()
        self.envelope_to_accounts = module.mappings_used
        self.primary_currency = module.get_primary_currency()
        self.price_map = module.price_map

        self.available_months = module.available_months
        self.available_months_str = [str(month) for month in self.available_months]

        self.ran_budget_df = True

    def get_budgets_months_available(self, currency):
        self.generate_budget_df(currency)
        return self.available_months_str

    def check_month_in_available_months(self, month, currency):
        return bool(month and month in self.get_budgets_months_available(currency))

    def get_currencies(self):
        if "currencies" in self.config:
            return self.config["currencies"]
        return None

    def generate_income_query_tables(self, month_str: str):
        primary_currency_amt_string = f"Amount ({self.primary_currency})"
        income_table_types = []
        income_table_types.append(("Name", str(str)))
        income_table_types.append((primary_currency_amt_string, str(Inventory)))
        income_table_types.append(("Amount", str(Inventory)))

        income_table_rows = []

        if month_str is not None:
            month = YearMonth.of_string(month_str)
            for name, amount in [
                ("Income this month", self.income_tables[month].avail_income),
                ("Funds from last month", self.income_tables[month].rolled_over),
                ("Budgeted for month", self.income_tables[month].budgeted),
                ("To be budgeted for month", self.income_tables[month].to_be_budgeted),
            ]:
                income_table_rows.append(
                    {
                        "Name": name,
                        primary_currency_amt_string: convert.convert_inventory_to_operating_currency(
                            amount,
                            self.price_map,
                            self.primary_currency,
                            month.last_day(),
                        ),
                        "Amount": amount,
                    }
                )

        return income_table_types, income_table_rows

    def generate_envelope_query_tables(self, month_str: str):
        envelope_table_types = []
        envelope_table_types.append(("Envelope", str(EnvelopeLink)))
        envelope_table_types.append(("Rolled over Allowence", str(Inventory)))
        envelope_table_types.append(("Budgeted", str(Inventory)))
        envelope_table_types.append(("Activity", str(Inventory)))
        envelope_table_types.append(("Available", str(Inventory)))

        envelope_table_rows = []

        if month_str is not None:
            month = YearMonth.of_string(month_str)
            for envelope_name, e_row in self.envelope_tables.items():
                if e_row[month].is_empty():
                    continue
                row = {}
                row["Envelope"] = EnvelopeLink(envelope_name, month_str, self.envelope_to_accounts[envelope_name])
                row["Rolled over Allowence"] = e_row[month.prev_month()].available
                row["Budgeted"] = e_row[month].budgeted
                row["Activity"] = e_row[month].activity
                row["Available"] = e_row[month].available
                envelope_table_rows.append(row)

        return envelope_table_types, envelope_table_rows
    
    @staticmethod
    def extra_escape(url: str):
        """
        
        Flask's url_for method does not escape some characters that Chrome (and mabe
        other browsers) try to replace, which causes unnecessary url navigations. Add
        extra escapes on top of that function. """

        # Have to ensure that the first ? character that separates the tags from the rest
        # of the url is not escaped.
        spl = url.split('?', maxsplit=1)
        if len(spl) == 1:
            return url
        
        escaped = (spl[1]
                .replace(':', r'%3A')
                .replace('$', r'%24')
                .replace("(", r"%28")
                .replace(")", r"%29")
                .replace("?", r"%3F")
                )
        
        return spl[0] + "?" + escaped

