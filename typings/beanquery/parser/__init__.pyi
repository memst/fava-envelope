"""
This type stub file was generated by pyright.
"""

import datetime
import decimal
import tatsu
from ..errors import ProgrammingError
from . import ast, parser

class BQLSemantics:
    def set_context(self, ctx): # -> None:
        ...
    
    def null(self, value): # -> None:
        ...
    
    def integer(self, value): # -> int:
        ...
    
    def decimal(self, value): # -> Decimal:
        ...
    
    def date(self, value): # -> _Date:
        ...
    
    def string(self, value):
        ...
    
    def boolean(self, value):
        ...
    
    def identifier(self, value):
        ...
    
    def asterisk(self, value): # -> Any:
        ...
    
    def list(self, value): # -> list[Any]:
        ...
    
    def ordering(self, value): # -> Ordering:
        ...
    


class ParseError(ProgrammingError):
    def __init__(self, parseinfo) -> None:
        ...
    


def parse(text):
    ...

