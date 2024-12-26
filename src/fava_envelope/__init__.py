from collections import defaultdict

from beancount.core.data import Account
from beancount.core.inventory import Inventory
from fava.context import g
from fava.ext import FavaExtensionBase

from fava_envelope.modules.beancount_envelope import BeancountEnvelope
from fava_envelope.modules.budgets import Envelope, Income
from fava_envelope.modules.year_month import YearMonth, YearMonthStr


class EnvelopeBudget(FavaExtensionBase):
    """The class handling the display of budgets in Fava."""

    # Stores whether the up-to-date version of the budget repors has been
    # cached.
    ran_budget_df: bool

    income_tables: defaultdict[YearMonth, Income]
    envelope_tables: defaultdict[Account, defaultdict[YearMonth, Envelope]]

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
        (self.income_tables, self.envelope_tables, _) = module.envelope_tables()

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
        income_table_types = []
        income_table_types.append(("Name", str(str)))
        income_table_types.append(("Amount", str(Inventory)))

        income_table_rows = []

        if month_str is not None:
            month = YearMonth.of_string(month_str)
            income_table_rows.append(
                {
                    "Name": "Funds for month",
                    "Amount": self.income_tables[month].avail_income,
                }
            )
            income_table_rows.append(
                {
                    "Name": "Overspent in prev month",
                    "Amount": self.income_tables[month].overspent,
                }
            )
            income_table_rows.append(
                {
                    "Name": "Budgeted for month",
                    "Amount": self.income_tables[month].budgeted,
                }
            )
            income_table_rows.append(
                {
                    "Name": "To be budgeted for month",
                    "Amount": self.income_tables[month].to_be_budgeted,
                }
            )
            income_table_rows.append(
                {
                    "Name": "Budgeted in the future",
                    "Amount": self.income_tables[month].budgeted_future,
                }
            )

        return income_table_types, income_table_rows

    def generate_envelope_query_tables(self, month_str: str):
        envelope_table_types = []
        envelope_table_types.append(("Account", str(str)))
        envelope_table_types.append(("Rolled over Allowence", str(Inventory)))
        envelope_table_types.append(("Budgeted", str(Inventory)))
        envelope_table_types.append(("Activity", str(Inventory)))
        envelope_table_types.append(("Available", str(Inventory)))

        envelope_table_rows = []

        if month_str is not None:
            month = YearMonth.of_string(month_str)
            for index, e_row in self.envelope_tables.items():
                row = {}
                row["Account"] = index
                row["Rolled over Allowence"] = e_row[month.prev_month()].available
                row["Budgeted"] = e_row[month].budgeted
                row["Activity"] = e_row[month].activity
                row["Available"] = e_row[month].available
                envelope_table_rows.append(row)

        return envelope_table_types, envelope_table_rows
