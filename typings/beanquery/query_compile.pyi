"""
This type stub file was generated by pyright.
"""

import dataclasses
import datetime
from decimal import Decimal
from dateutil.relativedelta import relativedelta
from beanquery.parser import ast
from beanquery import tables, types

"""Interpreter for the query language's AST.

This code accepts the abstract syntax tree produced by the query parser,
resolves the column and function names, compiles and interpreter and prepares a
query to be run against a list of entries.
"""
__copyright__ = ...
__license__ = ...
MARKER = ...
FUNCTIONS = ...
OPERATORS = ...
class EvalNode:
    __slots__ = ...
    def __init__(self, dtype) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        """Override the equality operator to compare the data type and a all attributes
        of this node. This is used by tests for comparing nodes.
        """
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def childnodes(self): # -> Generator[EvalNode, Any, None]:
        """Returns the child nodes of this node.
        Yields:
          A list of EvalNode instances.
        """
        ...
    
    def __call__(self, context):
        """Evaluate this node. This is designed to recurse on its children.
        All subclasses must override and implement this method.

        Args:
          context: The evaluation object to which the evaluation need to apply.
            This is either an entry, a Posting instance, or a particular result
            set row from a sub-select. This is the provider for the underlying
            data.
        Returns:
          The evaluated value for this sub-expression tree.
        """
        ...
    


class EvalConstant(EvalNode):
    __slots__ = ...
    def __init__(self, value, dtype=...) -> None:
        ...
    
    def __call__(self, _): # -> Any:
        ...
    


class EvalUnaryOp(EvalNode):
    __slots__ = ...
    def __init__(self, operator, operand, dtype) -> None:
        ...
    
    def __call__(self, context):
        ...
    
    def __repr__(self): # -> str:
        ...
    


class EvalUnaryOpSafe(EvalUnaryOp):
    def __call__(self, context): # -> None:
        ...
    


class EvalBinaryOp(EvalNode):
    __slots__ = ...
    def __init__(self, operator, left, right, dtype) -> None:
        ...
    
    def __call__(self, context): # -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class EvalBetween(EvalNode):
    __slots__ = ...
    def __init__(self, operand, lower, upper) -> None:
        ...
    
    def __call__(self, context): # -> None:
        ...
    


def unaryop(op, intypes, outtype, nullsafe=...): # -> Callable[..., Any]:
    ...

def binaryop(op, intypes, outtype): # -> Callable[..., Any]:
    ...

def Operator(op, operands):
    ...

@unaryop(ast.Neg, [int], int)
@unaryop(ast.Neg, [Decimal], Decimal)
def neg_(x):
    ...

@unaryop(ast.IsNull, [types.Any], bool, nullsafe=True)
def null(x): # -> bool:
    ...

@unaryop(ast.IsNotNull, [types.Any], bool, nullsafe=True)
def not_null(x): # -> bool:
    ...

@binaryop(ast.Mul, [Decimal, Decimal], Decimal)
@binaryop(ast.Mul, [Decimal, int], Decimal)
@binaryop(ast.Mul, [int, Decimal], Decimal)
@binaryop(ast.Mul, [int, int], int)
def mul_(x, y):
    ...

@binaryop(ast.Div, [Decimal, Decimal], Decimal)
@binaryop(ast.Div, [Decimal, int], Decimal)
@binaryop(ast.Div, [int, Decimal], Decimal)
def div_(x, y): # -> None:
    ...

@binaryop(ast.Div, [int, int], Decimal)
def div_int(x, y): # -> None:
    ...

@binaryop(ast.Mod, [int, int], int)
@binaryop(ast.Mod, [Decimal, int], Decimal)
@binaryop(ast.Mod, [int, Decimal], Decimal)
@binaryop(ast.Mod, [Decimal, Decimal], Decimal)
def mod_(x, y): # -> None:
    ...

@binaryop(ast.Add, [Decimal, Decimal], Decimal)
@binaryop(ast.Add, [Decimal, int], Decimal)
@binaryop(ast.Add, [int, Decimal], Decimal)
@binaryop(ast.Add, [int, int], int)
@binaryop(ast.Add, [datetime.date, relativedelta], datetime.date)
@binaryop(ast.Add, [relativedelta, datetime.date], datetime.date)
@binaryop(ast.Add, [relativedelta, relativedelta], relativedelta)
def add_(x, y):
    ...

@binaryop(ast.Sub, [Decimal, Decimal], Decimal)
@binaryop(ast.Sub, [Decimal, int], Decimal)
@binaryop(ast.Sub, [int, Decimal], Decimal)
@binaryop(ast.Sub, [int, int], int)
@binaryop(ast.Sub, [datetime.date, relativedelta], datetime.date)
@binaryop(ast.Sub, [relativedelta, datetime.date], datetime.date)
@binaryop(ast.Sub, [relativedelta, relativedelta], datetime.date)
def sub_(x, y):
    ...

@binaryop(ast.Add, [datetime.date, int], datetime.date)
def add_date_int(x, y):
    ...

@binaryop(ast.Add, [int, datetime.date], datetime.date)
def add_int_date(x, y):
    ...

@binaryop(ast.Sub, [datetime.date, int], datetime.date)
def sub_date_int(x, y):
    ...

@binaryop(ast.Sub, [datetime.date, datetime.date], int)
def sub_date_date(x, y):
    ...

@binaryop(ast.Match, [str, str], bool)
def match_(x, y): # -> bool:
    ...

@binaryop(ast.NotMatch, [str, str], bool)
def not_match_(x, y): # -> bool:
    ...

@binaryop(ast.In, [types.Any, set], bool)
@binaryop(ast.In, [types.Any, list], bool)
@binaryop(ast.In, [types.Any, dict], bool)
def in_(x, y): # -> bool:
    ...

@binaryop(ast.NotIn, [types.Any, set], bool)
@binaryop(ast.NotIn, [types.Any, list], bool)
@binaryop(ast.NotIn, [types.Any, dict], bool)
def not_in_(x, y): # -> bool:
    ...

_comparisons = ...
_intypes = ...
_comparable = ...
class EvalAnd(EvalNode):
    __slots__ = ...
    def __init__(self, args) -> None:
        ...
    
    def __call__(self, context): # -> bool | None:
        ...
    


class EvalOr(EvalNode):
    __slots__ = ...
    def __init__(self, args) -> None:
        ...
    
    def __call__(self, context): # -> bool | None:
        ...
    


class EvalCoalesce(EvalNode):
    __slots__ = ...
    def __init__(self, args) -> None:
        ...
    
    def __call__(self, context): # -> None:
        ...
    


class EvalFunction(EvalNode):
    __slots__ = ...
    __intypes__ = ...
    def __init__(self, context, operands, dtype) -> None:
        ...
    


class EvalGetItem(EvalNode):
    __slots__ = ...
    def __init__(self, operand, key) -> None:
        ...
    
    def __call__(self, context): # -> None:
        ...
    


class EvalGetter(EvalNode):
    __slots__ = ...
    def __init__(self, operand, getter, dtype) -> None:
        ...
    
    def __call__(self, context): # -> None:
        ...
    


class EvalColumn(EvalNode):
    ...


class EvalAggregator(EvalFunction):
    pure = ...
    def __init__(self, context, operands, dtype=...) -> None:
        ...
    
    def allocate(self, allocator): # -> None:
        """Allocate handles to store data for a node's aggregate storage.

        This is called once before beginning aggregations. If you need any
        kind of per-aggregate storage during the computation phase, get it
        in this method.

        Args:
          allocator: An instance of Allocator, on which you can call allocate() to
            obtain a handle for a slot to store data on store objects later on.
        """
        ...
    
    def initialize(self, store): # -> None:
        """Initialize this node's aggregate data.

        Args:
          store: An object indexable by handles appropriated during allocate().
        """
        ...
    
    def update(self, store, context): # -> None:
        """Evaluate this node. This is designed to recurse on its children.

        Args:
          store: An object indexable by handles appropriated during allocate().
          context: The object to which the evaluation need to apply (see __call__).
        """
        ...
    
    def finalize(self, store): # -> None:
        """Finalize this node's aggregate data.

        Args:
          store: An object indexable by handles appropriated during allocate().
        """
        ...
    
    def __call__(self, context): # -> None:
        """Return the value on evaluation.

        Args:
          context: The evaluation object to which the evaluation need to apply.
        Returns:
          The final aggregated value.
        """
        ...
    


class SubqueryTable(tables.Table):
    def __init__(self, subquery) -> None:
        ...
    
    @staticmethod
    def column(i, name, dtype): # -> type[Column]:
        class Column(EvalColumn):
            ...
        
        
    
    def __iter__(self): # -> Iterator[tuple[Any, ...]]:
        ...
    


class EvalConstantSubquery1D(EvalNode):
    def __init__(self, subquery) -> None:
        ...
    
    def __call__(self, context): # -> list[Any] | object | None:
        ...
    


EvalTarget = ...
@dataclasses.dataclass
class EvalQuery:
    table: tables.Table
    c_targets: list
    c_where: EvalNode
    group_indexes: list[int]
    having_index: int
    order_spec: list[tuple[int, ast.Ordering]]
    limit: int
    distinct: bool
    @property
    def columns(self): # -> list[Any]:
        ...
    


EvalPivot = ...
EvalPrint = ...
