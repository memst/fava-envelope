from dataclasses import dataclass


@dataclass
class EnvelopeLink:
    name: str
    year_month:str
    linked_accounts: str

    def __init__(self, name: str, year_month:str, used_mappings:set[str]):
        self.name = name
        self.year_month=year_month
        self.linked_accounts = f"^(?:{'|'.join(used_mappings)})$"