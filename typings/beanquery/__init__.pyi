"""
This type stub file was generated by pyright.
"""

import importlib
from urllib.parse import urlparse
from . import compiler, parser, tables
from .compiler import CompilationError
from .cursor import Column, Cursor
from .errors import DataError, DatabaseError, Error, IntegrityError, InterfaceError, InternalError, NotSupportedError, OperationalError, ProgrammingError, Warning
from .parser import ParseError

__version__ = ...
apilevel = ...
threadsafety = ...
paramstyle = ...
def connect(dsn, **kwargs): # -> Connection:
    ...

class Connection:
    def __init__(self, dsn=..., **kwargs) -> None:
        ...
    
    def attach(self, dsn, **kwargs): # -> None:
        ...
    
    def close(self): # -> None:
        ...
    
    def parse(self, query):
        ...
    
    def compile(self, query): # -> None:
        ...
    
    def execute(self, query, params=...): # -> Cursor:
        ...
    
    def cursor(self): # -> Cursor:
        ...
    


__all__ = ['Column', 'CompilationError', 'Connection', 'Cursor', 'DataError', 'DatabaseError', 'Error', 'IntegrityError', 'InterfaceError', 'InternalError', 'NotSupportedError', 'OperationalError', 'ParseError', 'ProgrammingError', 'Warning', 'apilevel', 'connet', 'paramstyle', 'threadsafety']
