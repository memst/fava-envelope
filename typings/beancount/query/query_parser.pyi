"""
This type stub file was generated by pyright.
"""

"""Parser for Beancount Query Language.
"""
__copyright__ = ...
__license__ = ...
Select = ...
Balances = ...
Journal = ...
Print = ...
Errors = ...
Reload = ...
Explain = ...
RunCustom = ...
Target = ...
Wildcard = ...
From = ...
GroupBy = ...
OrderBy = ...
PivotBy = ...
Column = ...
Function = ...
Constant = ...
UnaryOp = ...
class Not(UnaryOp):
    ...


BinaryOp = ...
class And(BinaryOp):
    ...


class Or(BinaryOp):
    ...


class Equal(BinaryOp):
    ...


class Greater(BinaryOp):
    ...


class GreaterEq(BinaryOp):
    ...


class Less(BinaryOp):
    ...


class LessEq(BinaryOp):
    ...


class Match(BinaryOp):
    ...


class Contains(BinaryOp):
    ...


class Mul(BinaryOp):
    ...


class Div(BinaryOp):
    ...


class Add(BinaryOp):
    ...


class Sub(BinaryOp):
    ...


class ParseError(Exception):
    """A parser error."""
    ...


class Lexer:
    """PLY lexer for the Beancount Query Language.
    """
    keywords = ...
    tokens = ...
    def t_ID(self, token):
        "[a-zA-Z][a-zA-Z_]*"
        ...
    
    def t_STRING(self, token):
        "(\"[^\"]*\"|\'[^\']*\')"
        ...
    
    def t_DATE(self, token):
        r"(\#(\"[^\"]*\"|\'[^\']*\')|\d\d\d\d-\d\d-\d\d)"
        ...
    
    t_COMMA = ...
    t_SEMI = ...
    t_LPAREN = ...
    t_RPAREN = ...
    t_NE = ...
    t_EQ = ...
    t_GTE = ...
    t_GT = ...
    t_LTE = ...
    t_LT = ...
    t_TILDE = ...
    t_ASTERISK = ...
    t_SLASH = ...
    t_PLUS = ...
    t_MINUS = ...
    def t_DECIMAL(self, token):
        r"[-+]?([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)"
        ...
    
    def t_INTEGER(self, token):
        r"[-+]?[0-9]+"
        ...
    
    t_ignore = ...
    def t_error(self, token):
        ...
    


class SelectParser(Lexer):
    """PLY parser for the Beancount Query Language's SELECT statement.
    """
    start = ...
    def __init__(self, **options) -> None:
        ...
    
    def tokenize(self, line): # -> None:
        ...
    
    def parse(self, line, debug=..., default_close_date=...):
        ...
    
    def handle_comma_separated_list(self, p): # -> list[Any]:
        """Handle a list of 0, 1 or more comma-separated values.
        Args:
          p: A grammar object.
        """
        ...
    
    def p_account(self, p): # -> None:
        """
        account : STRING
        """
        ...
    
    def p_select_statement(self, p): # -> None:
        """
        select_statement : SELECT distinct target_spec from_subselect where \
                           group_by order_by pivot_by limit flatten
        """
        ...
    
    def p_distinct(self, p): # -> None:
        """
        distinct : empty
                 | DISTINCT
        """
        ...
    
    def p_target_spec(self, p): # -> None:
        """
        target_spec : ASTERISK
                    | target_list
        """
        ...
    
    def p_target_list(self, p): # -> None:
        """
        target_list : target
                    | target_list COMMA target
        """
        ...
    
    def p_target(self, p): # -> None:
        """
        target : expression AS ID
               | expression
        """
        ...
    
    def p_from(self, p): # -> None:
        """
        from : empty
             | FROM opt_expression opt_open opt_close opt_clear
        """
        ...
    
    def p_from_subselect(self, p): # -> None:
        """
        from_subselect : from
                       | FROM LPAREN select_statement RPAREN
        """
        ...
    
    def p_opt_open(self, p): # -> None:
        """
        opt_open : empty
                 | OPEN ON DATE
        """
        ...
    
    def p_opt_close(self, p): # -> None:
        """
        opt_close : empty
                  | CLOSE
                  | CLOSE ON DATE
        """
        ...
    
    def p_opt_clear(self, p): # -> None:
        """
        opt_clear : empty
                  | CLEAR
        """
        ...
    
    def p_where(self, p): # -> None:
        """
        where : empty
              | WHERE expression
        """
        ...
    
    def p_expr_index_list(self, p): # -> None:
        """
        expr_index_list : expr_index
                        | expr_index_list COMMA expr_index
        """
        ...
    
    def p_expr_index(self, p): # -> None:
        """
        expr_index : expression
                   | INTEGER
        """
        ...
    
    def p_group_by(self, p): # -> None:
        """
        group_by : empty
                 | GROUP BY expr_index_list having
        """
        ...
    
    def p_having(self, p): # -> None:
        """
        having : empty
               | HAVING expression
        """
        ...
    
    def p_order_by(self, p): # -> None:
        """
        order_by : empty
                 | ORDER BY expr_index_list ordering
        """
        ...
    
    def p_ordering(self, p): # -> None:
        """
        ordering : empty
                 | ASC
                 | DESC
        """
        ...
    
    def p_pivot_by(self, p): # -> None:
        """
        pivot_by : empty
                 | PIVOT BY column_list
        """
        ...
    
    def p_limit(self, p): # -> None:
        """
        limit : empty
              | LIMIT INTEGER
        """
        ...
    
    def p_flatten(self, p): # -> None:
        """
        flatten : empty
                | FLATTEN
        """
        ...
    
    precedence = ...
    def p_expression_and(self, p): # -> None:
        "expression : expression AND expression"
        ...
    
    def p_expression_or(self, p): # -> None:
        "expression : expression OR expression"
        ...
    
    def p_expression_not(self, p): # -> None:
        "expression : NOT expression"
        ...
    
    def p_expression_paren(self, p): # -> None:
        "expression : LPAREN expression RPAREN"
        ...
    
    def p_expression_eq(self, p): # -> None:
        "expression : expression EQ expression"
        ...
    
    def p_expression_ne(self, p): # -> None:
        "expression : expression NE expression"
        ...
    
    def p_expression_gt(self, p): # -> None:
        "expression : expression GT expression"
        ...
    
    def p_expression_gte(self, p): # -> None:
        "expression : expression GTE expression"
        ...
    
    def p_expression_lt(self, p): # -> None:
        "expression : expression LT expression"
        ...
    
    def p_expression_lte(self, p): # -> None:
        "expression : expression LTE expression"
        ...
    
    def p_expression_match(self, p): # -> None:
        "expression : expression TILDE expression"
        ...
    
    def p_expression_contains(self, p): # -> None:
        "expression : expression IN expression"
        ...
    
    def p_expression_column(self, p): # -> None:
        "expression : column"
        ...
    
    def p_expression_constant(self, p): # -> None:
        "expression : constant"
        ...
    
    def p_expression_mul(self, p): # -> None:
        "expression : expression ASTERISK expression"
        ...
    
    def p_expression_div(self, p): # -> None:
        "expression : expression SLASH expression"
        ...
    
    def p_expression_add(self, p): # -> None:
        "expression : expression PLUS expression"
        ...
    
    def p_expression_sub(self, p): # -> None:
        "expression : expression MINUS expression"
        ...
    
    def p_expression_function(self, p): # -> None:
        "expression : ID LPAREN expression_list_opt RPAREN"
        ...
    
    def p_opt_expression(self, p): # -> None:
        """
        opt_expression : empty
                       | expression
        """
        ...
    
    def p_expression_list_opt(self, p): # -> None:
        """
        expression_list_opt : empty
                            | expression
                            | expression_list COMMA expression
        """
        ...
    
    def p_expression_list(self, p): # -> None:
        """
        expression_list : expression
                        | expression_list COMMA expression
        """
        ...
    
    def p_column(self, p): # -> None:
        """
        column : ID
        """
        ...
    
    def p_column_list(self, p): # -> None:
        """
        column_list : column
                    | column_list COMMA column
        """
        ...
    
    def p_constant(self, p): # -> None:
        """
        constant : NULL
                 | boolean
                 | INTEGER
                 | DECIMAL
                 | STRING
                 | DATE
        """
        ...
    
    def p_boolean(self, p): # -> None:
        """
        boolean : TRUE
                | FALSE
        """
        ...
    
    def p_empty(self, _): # -> None:
        """
        empty :
        """
        ...
    
    def p_error(self, token):
        ...
    


class Parser(SelectParser):
    """PLY parser for the Beancount Query Language's full command syntax.
    """
    start = ...
    def p_regular_statement(self, p): # -> None:
        "top_statement : statement delimiter"
        ...
    
    def p_explain_statement(self, p): # -> None:
        "top_statement : EXPLAIN statement delimiter"
        ...
    
    def p_statement(self, p): # -> None:
        """
        statement : select_statement
                  | balances_statement
                  | journal_statement
                  | print_statement
                  | run_statement
                  | errors_statement
                  | reload_statement
        """
        ...
    
    def p_delimiter(self, p): # -> None:
        """
        delimiter : SEMI
                  | empty
        """
        ...
    
    def p_balances_statement(self, p): # -> None:
        """
        balances_statement : BALANCES summary_func from where
        """
        ...
    
    def p_journal_statement(self, p): # -> None:
        """
        journal_statement : JOURNAL summary_func from
                          | JOURNAL account summary_func from
        """
        ...
    
    def p_summary_func(self, p): # -> None:
        """
        summary_func : empty
                     | AT ID
        """
        ...
    
    def p_print_statement(self, p): # -> None:
        """
        print_statement : PRINT from
        """
        ...
    
    def p_run_statement(self, p): # -> None:
        """
        run_statement : RUN ID
                      | RUN STRING
                      | RUN ASTERISK
                      | RUN empty
        """
        ...
    
    def p_errors_statement(self, p): # -> None:
        """
        errors_statement : ERRORS
        """
        ...
    
    def p_reload_statement(self, p): # -> None:
        """
        reload_statement : RELOAD
        """
        ...
    


def get_expression_name(expr): # -> LiteralString | str:
    """Come up with a reasonable identifier for an expression.

    Args:
      expr: An expression node.
    """
    ...
