"""
This type stub file was generated by pyright.
"""

import cmd
import click
import beancount
import beanquery
from dataclasses import dataclass
from beancount.utils import pager

__copyright__ = ...
__license__ = ...
HISTORY_FILENAME = ...
INIT_FILENAME = ...
class style:
    ERROR = ...
    WARNING = ...
    RESET = ...
    ESCAPES = ...
    @classmethod
    def strip(cls, x): # -> str:
        ...
    


def render_location(text, pos, endpos, lineno, indent, strip, out): # -> None:
    ...

def render_exception(exc, indent=..., strip=...): # -> str:
    ...

FORMATS = ...
@dataclass
class Settings:
    boxed: bool = ...
    expand: bool = ...
    format: str = ...
    narrow: bool = ...
    nullvalue: str = ...
    numberify: bool = ...
    pager: bool = ...
    spaced: bool = ...
    unicode: bool = ...
    def getstr(self, name): # -> str:
        ...
    
    def setstr(self, name, value): # -> None:
        ...
    
    def todict(self): # -> dict[str, Any]:
        ...
    
    def __iter__(self): # -> Iterator[str]:
        ...
    


class DispatchingShell(cmd.Cmd):
    """A usable convenient shell for interpreting commands, with history."""
    doc_header = ...
    misc_header = ...
    def __init__(self, outfile, interactive, runinit, settings) -> None:
        """Create a shell with history.

        Args:
          outfile: An output file object to write communications to.
          interactive: A boolean, true if this serves an interactive tty.
          runinit: When true, execute the commands from the user init file.
          settings: The shell settings.
        """
        ...
    
    def echo(self, message, file=...): # -> None:
        ...
    
    def error(self, message): # -> None:
        ...
    
    def warning(self, message, *args): # -> None:
        ...
    
    def add_help(self): # -> None:
        "Attach help functions for each of the parsed token handlers."
        ...
    
    @property
    def output(self): # -> nullcontext[None]:
        """Where to direct command output.

        When the output stream is connected to the standard output,
        and we are running interactively, use an indirection that can
        send the output to a pager when the number of lines emitted is
        greater than a threshold.

        Returns:
          A context manager that returns a file descriptor on enter.

        """
        ...
    
    def cmdloop(self, intro=...): # -> None:
        """Override cmdloop to handle keyboard interrupts."""
        ...
    
    def parseline(self, line): # -> tuple[Literal[''] | None, str | None, str] | tuple[str, str | None, str]:
        ...
    
    def onecmd(self, line): # -> Any | None:
        ...
    
    def completenames(self, text, *ignored): # -> list[str] | None:
        ...
    
    def do_help(self, arg): # -> None:
        """List available commands with "help" or detailed help with "help cmd"."""
        ...
    
    def do_history(self, arg): # -> None:
        """Print the command-line history."""
        ...
    
    def do_clear(self, arg): # -> None:
        """Clear the command-line history."""
        ...
    
    def do_set(self, arg): # -> None:
        """Set shell settings variables."""
        ...
    
    def complete_set(self, text, _line, _begidx, _endidx): # -> list[Any]:
        ...
    
    def do_parse(self, arg): # -> None:
        """Run the parser on the following command and print the output."""
        ...
    
    def parse(self, query, **kwargs):
        ...
    
    def execute(self, query, **kwargs): # -> Any:
        """Handle statements via our parser instance and dispatch to appropriate methods.

        Args:
          query: The string to be parsed.
        """
        ...
    
    def do_exit(self, arg): # -> Literal[True]:
        """Exit the command interpreter."""
        ...
    
    do_quit = ...
    def do_EOF(self, arg): # -> Literal[True]:
        """Exit the command interpreter."""
        ...
    


class BQLShell(DispatchingShell):
    """An interactive shell interpreter for the Beancount query language."""
    prompt = ...
    def __init__(self, filename, outfile, interactive=..., runinit=..., format=..., numberify=...) -> None:
        ...
    
    def parse(self, line, default_close_date=..., **kwargs):
        ...
    
    def do_reload(self, arg=...): # -> None:
        "Reload the Beancount input file."
        ...
    
    def do_errors(self, arg=...): # -> None:
        "Print the errors that occurred during Beancount input file parsing."
        ...
    
    def do_run(self, arg): # -> None:
        "Run a named query defined in the Beancount input file."
        ...
    
    def complete_run(self, text, line, begidx, endidx): # -> list[Any]:
        ...
    
    def do_tables(self, arg): # -> None:
        """List tables."""
        ...
    
    def do_describe(self, arg): # -> None:
        """Describe table or structured type."""
        ...
    
    def complete_describe(self, text, line, begidx, endidx): # -> list[str]:
        ...
    
    def do_explain(self, arg):
        """Compile and print a compiled statement for debugging."""
        ...
    
    def on_Print(self, statement): # -> None:
        """
        Print entries in Beancount format.

        The general form of a PRINT statement includes an SQL-like FROM
        selector:

           PRINT [FROM <from_expr> ...]

        Where:

          from_expr: A logical expression that matches on the attributes of
            the directives. See SELECT command for details (this FROM expression
            supports all the same expressions including its OPEN, CLOSE and
            CLEAR operations).

        """
        ...
    
    def on_Select(self, statement): # -> Any:
        """
        Extract data from a query on the postings.

        The general form of a SELECT statement loosely follows SQL syntax, with
        some mild and idiomatic extensions:

           SELECT [DISTINCT] [<targets>|*]
           [FROM <from_expr> [OPEN ON <date>] [CLOSE [ON <date>]] [CLEAR]]
           [WHERE <where_expr>]
           [GROUP BY <groups>]
           [ORDER BY <groups> [ASC|DESC]]
           [LIMIT num]

        Where:

          targets: A list of desired output attributes from the postings, and
            expressions on them. Some of the attributes of the parent transaction
            directive are made available in this context as well. Simple functions
            (that return a single value per row) and aggregation functions (that
            return a single value per group) are available. For the complete
            list of supported columns and functions, see help on "targets".
            You can also provide a wildcard here, which will select a reasonable
            default set of columns for rendering a journal.

          from_expr: A logical expression that matches on the attributes of
            the directives (not postings). This allows you to select a subset of
            transactions, so the accounting equation is respected for balance
            reports. For the complete list of supported columns and functions,
            see help on "from".

          where_expr: A logical expression that matches on the attributes of
            postings. The available columns are similar to those in the targets
            clause, without the aggregation functions.

          OPEN clause: replace all the transactions before the given date by
            summarizing entries and transfer Income and Expenses balances to
            Equity.

          CLOSE clause: Remove all the transactions after the given date and

          CLEAR: Transfer final Income and Expenses balances to Equity.

        """
        ...
    
    def on_Journal(self, journal): # -> Any:
        """
        Select a journal of some subset of postings. This command is a
        convenience and converts into an equivalent Select statement, designed
        to extract the most sensible list of columns for the register of a list
        of entries as a table.

        The general form of a JOURNAL statement loosely follows SQL syntax:

           JOURNAL <account-regexp> [FROM_CLAUSE]

        See the SELECT query help for more details on the FROM clause.
        """
        ...
    
    def on_Balances(self, balance): # -> Any:
        """
        Select balances of some subset of postings. This command is a
        convenience and converts into an equivalent Select statement, designed
        to extract the most sensible list of columns for the register of a list
        of entries as a table.

        The general form of a JOURNAL statement loosely follows SQL syntax:

           BALANCE [FROM_CLAUSE]

        See the SELECT query help for more details on the FROM clause.
        """
        ...
    
    def help_targets(self): # -> None:
        ...
    
    def help_from(self): # -> None:
        ...
    
    def help_where(self): # -> None:
        ...
    


def summary_statistics(entries): # -> tuple[int, int, int]:
    """Calculate basic summary statistics to output a brief welcome message.

    Args:
      entries: A list of directives.
    Returns:
      A tuple of three integers, the total number of directives parsed, the total number
      of transactions and the total number of postings there in.
    """
    ...

def print_statistics(entries, options, outfile): # -> None:
    """Print summary statistics to stdout.

    Args:
      entries: A list of directives.
      options: An options map. as produced by the parser.
      outfile: A file object to write to.
    """
    ...

@click.command()
@click.argument('filename')
@click.argument('query', nargs=-1)
@click.option('--numberify', '-m', is_flag=True, help="Numberify the output, removing the currencies.")
@click.option('--format', '-f', type=click.Choice(FORMATS.keys()), default='text', help="Output format.")
@click.option('--output', '-o', type=click.File('w'), default='-', help="Output filename.")
@click.option('--no-errors', '-q', is_flag=True, help="Do not report errors.")
@click.version_option('', message=f'beanquery {beanquery.__version__}, beancount {beancount.__version__}')
def main(filename, query, numberify, format, output, no_errors): # -> None:
    """An interactive interpreter for the Beancount Query Language.

    Load Beancount ledger FILENAME and run Beancount Query Language
    QUERY on it, if specified, or drop into the interactive shell. If
    not explicitly set with the dedicated option, the output format is
    inferred from the output file name, if specified.

    """
    ...
