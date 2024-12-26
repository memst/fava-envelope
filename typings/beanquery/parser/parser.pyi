"""
This type stub file was generated by pyright.
"""

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.infos import ParserConfig

KEYWORDS = ...
class BQLBuffer(Buffer):
    def __init__(self, text, /, config: ParserConfig = ..., **settings) -> None:
        ...
    


class BQLParser(Parser):
    def __init__(self, /, config: ParserConfig = ..., **settings) -> None:
        ...
    


class BQLSemantics:
    def bql(self, ast):
        ...
    
    def statement(self, ast):
        ...
    
    def select(self, ast):
        ...
    
    def subselect(self, ast):
        ...
    
    def from_(self, ast):
        ...
    
    def table(self, ast):
        ...
    
    def groupby(self, ast):
        ...
    
    def order(self, ast):
        ...
    
    def ordering(self, ast):
        ...
    
    def pivotby(self, ast):
        ...
    
    def target(self, ast):
        ...
    
    def expression(self, ast):
        ...
    
    def disjunction(self, ast):
        ...
    
    def or_(self, ast):
        ...
    
    def conjunction(self, ast):
        ...
    
    def and_(self, ast):
        ...
    
    def inversion(self, ast):
        ...
    
    def not_(self, ast):
        ...
    
    def comparison(self, ast):
        ...
    
    def lt(self, ast):
        ...
    
    def lte(self, ast):
        ...
    
    def gt(self, ast):
        ...
    
    def gte(self, ast):
        ...
    
    def eq(self, ast):
        ...
    
    def neq(self, ast):
        ...
    
    def in_(self, ast):
        ...
    
    def notin(self, ast):
        ...
    
    def match(self, ast):
        ...
    
    def notmatch(self, ast):
        ...
    
    def isnull(self, ast):
        ...
    
    def isnotnull(self, ast):
        ...
    
    def between(self, ast):
        ...
    
    def sum(self, ast):
        ...
    
    def add(self, ast):
        ...
    
    def sub(self, ast):
        ...
    
    def term(self, ast):
        ...
    
    def mul(self, ast):
        ...
    
    def div(self, ast):
        ...
    
    def mod(self, ast):
        ...
    
    def factor(self, ast):
        ...
    
    def unary(self, ast):
        ...
    
    def uplus(self, ast):
        ...
    
    def uminus(self, ast):
        ...
    
    def primary(self, ast):
        ...
    
    def attribute(self, ast):
        ...
    
    def subscript(self, ast):
        ...
    
    def atom(self, ast):
        ...
    
    def placeholder(self, ast):
        ...
    
    def function(self, ast):
        ...
    
    def column(self, ast):
        ...
    
    def literal(self, ast):
        ...
    
    def constant(self, ast):
        ...
    
    def list(self, ast):
        ...
    
    def identifier(self, ast):
        ...
    
    def asterisk(self, ast):
        ...
    
    def string(self, ast):
        ...
    
    def boolean(self, ast):
        ...
    
    def null(self, ast):
        ...
    
    def integer(self, ast):
        ...
    
    def decimal(self, ast):
        ...
    
    def date(self, ast):
        ...
    
    def balances(self, ast):
        ...
    
    def journal(self, ast):
        ...
    
    def print(self, ast):
        ...
    


def main(filename, **kwargs):
    ...

if __name__ == '__main__':
    ast = ...
    data = ...