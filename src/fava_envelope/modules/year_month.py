import calendar
import datetime
from dataclasses import dataclass

YearMonthStr = str


@dataclass(order=True, frozen=True)
class YearMonth:
    year: int
    month: int

    def __post_init__(self):
        if not (1 <= self.month <= 12):
            raise ValueError(f"Invalid month {self.month}")

    def __str__(self):
        return f"{self.year}-{self.month:02}"

    def to_string(self) -> YearMonthStr:
        return str(self)

    @classmethod
    def of_date(cls, date: datetime.date):
        return cls(date.year, date.month)

    @classmethod
    def of_string(cls, date: str):
        year, month = date.split("-")
        return cls(int(year), int(month))

    def first_day(self):
        return datetime.date(self.year, self.month, 1)

    def last_day(self):
        return datetime.date(
            self.year, self.month, calendar.monthrange(self.year, self.month)[1]
        )

    def next_month(self):
        if self.month < 12:
            return YearMonth(self.year, self.month + 1)
        else:
            return YearMonth(self.year + 1, self.month - 11)

    def prev_month(self):
        if self.month > 1:
            return YearMonth(self.year, self.month - 1)
        else:
            return YearMonth(self.year - 1, self.month + 11)


def months_between(start: YearMonth, end: YearMonth):
    while start <= end:
        yield start
        start = start.next_month()
