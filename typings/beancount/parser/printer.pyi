"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
__copyright__ = ...
__license__ = ...
def align_position_strings(strings):
    """A helper used to align rendered amounts positions to their first currency
    character (an uppercase letter). This class accepts a list of rendered
    positions and calculates the necessary width to render them stacked in a
    column so that the first currency word aligns. It does not go beyond that
    (further currencies, e.g. for the price or cost, are not aligned).

    This is perhaps best explained with an example. The following positions will
    be aligned around the column marked with '^':

              45 HOOL {504.30 USD}
               4 HOOL {504.30 USD, 2014-11-11}
            9.95 USD
       -22473.32 CAD @ 1.10 USD
                 ^

    Strings without a currency character will be rendered flush left.

    Args:
      strings: A list of rendered position or amount strings.
    Returns:
      A pair of a list of aligned strings and the width of the aligned strings.
    """
    ...

class EntryPrinter:
    """A multi-method interface for printing all directive types.

    Attributes:
      dcontext: An instance of DisplayContext with which to render all the numbers.
      render_weight: A boolean, true if we should render the weight of the postings
        as a comment, for debugging.
      min_width_account: An integer, the minimum width to leave for the account name.
      prefix: User-specific prefix for custom indentation (for Fava).
      stringify_invalid_types: If a metadata value is invalid, force a conversion to
        string for printout.
    """
    def __init__(self, dcontext=..., render_weight=..., min_width_account=..., prefix=..., stringify_invalid_types=...) -> None:
        ...
    
    def __call__(self, obj):
        """Render a directive.

        Args:
          obj: The directive to be rendered.
        Returns:
          A string, the rendered directive.
        """
        ...
    
    META_IGNORE = ...
    def write_metadata(self, meta, oss, prefix=...):
        """Write metadata to the file object, excluding filename and line number.

        Args:
          meta: A dict that contains the metadata for this directive.
          oss: A file object to write to.
        """
        ...
    
    def Transaction(self, entry, oss):
        ...
    
    def render_posting_strings(self, posting):
        """This renders the three components of a posting: the account and its optional
        posting flag, the position, and finally, the weight of the position. The
        purpose is to align these in the caller.

        Args:
          posting: An instance of Posting, the posting to render.
        Returns:
          A tuple of
            flag_account: A string, the account name including the flag.
            position_str: A string, the rendered position string.
            weight_str: A string, the rendered weight of the posting.
        """
        ...
    
    def Posting(self, posting, oss):
        ...
    
    def Balance(self, entry, oss):
        ...
    
    def Note(self, entry, oss):
        ...
    
    def Document(self, entry, oss):
        ...
    
    def Pad(self, entry, oss):
        ...
    
    def Open(self, entry, oss):
        ...
    
    def Close(self, entry, oss):
        ...
    
    def Commodity(self, entry, oss):
        ...
    
    def Price(self, entry, oss):
        ...
    
    def Event(self, entry, oss):
        ...
    
    def Query(self, entry, oss):
        ...
    
    def Custom(self, entry, oss):
        ...
    


def format_entry(entry, dcontext=..., render_weights=..., prefix=...):
    """Format an entry into a string in the same input syntax the parser accepts.

    Args:
      entry: An entry instance.
      dcontext: An instance of DisplayContext used to format the numbers.
      render_weights: A boolean, true to render the weights for debugging.
    Returns:
      A string, the formatted entry.
    """
    ...

def print_entry(entry, dcontext=..., render_weights=..., file=...):
    """A convenience function that prints a single entry to a file.

    Args:
      entry: A directive entry.
      dcontext: An instance of DisplayContext used to format the numbers.
      render_weights: A boolean, true to render the weights for debugging.
      file: An optional file object to write the entries to.
    """
    ...

def print_entries(entries, dcontext=..., render_weights=..., file=..., prefix=...):
    """A convenience function that prints a list of entries to a file.

    Args:
      entries: A list of directives.
      dcontext: An instance of DisplayContext used to format the numbers.
      render_weights: A boolean, true to render the weights for debugging.
      file: An optional file object to write the entries to.
    """
    ...

def render_source(meta):
    """Render the source for errors in a way that it will be both detected by
    Emacs and align and rendered nicely.

    Args:
      meta: A dict with the metadata.
    Returns:
      A string, rendered to be interpretable as a message location for Emacs or
      other editors.
    """
    ...

def format_error(error):
    """Given an error objects, return a formatted string for it.

    Args:
      error: a namedtuple objects representing an error. It has to have an
        'entry' attribute that may be either a single directive object or a
        list of directive objects.
    Returns:
      A string, the errors rendered.
    """
    ...

def print_error(error, file=...):
    """A convenience function that prints a single error to a file.

    Args:
      error: An error object.
      file: An optional file object to write the errors to.
    """
    ...

def print_errors(errors, file=..., prefix=...):
    """A convenience function that prints a list of errors to a file.

    Args:
      errors: A list of errors.
      file: An optional file object to write the errors to.
    """
    ...

