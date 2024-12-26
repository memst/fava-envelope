"""
This type stub file was generated by pyright.
"""

"""Functions that operate on account strings.

These account objects are rather simple and dumb; they do not contain the list
of their associated postings. This is achieved by building a realization; see
realization.py for details.
"""
__copyright__ = ...
__license__ = ...
sep = ...
ACC_COMP_TYPE_RE = ...
ACC_COMP_NAME_RE = ...
ACCOUNT_RE = ...
TYPE = ...
def is_valid(string): # -> bool:
    """Return true if the given string is a valid account name.
    This does not check for the root account types, just the general syntax.

    Args:
      string: A string, to be checked for account name pattern.
    Returns:
      A boolean, true if the string has the form of an account's name.
    """
    ...

def join(*components): # -> str:
    """Join the names with the account separator.

    Args:
      *components: Strings, the components of an account name.
    Returns:
      A string, joined in a single account name.
    """
    ...

def split(account_name):
    """Split an account's name into its components.

    Args:
      account_name: A string, an account name.
    Returns:
      A list of strings, the components of the account name (without the separators).
    """
    ...

def parent(account_name): # -> str | None:
    """Return the name of the parent account of the given account.

    Args:
      account_name: A string, the name of the account whose parent to return.
    Returns:
      A string, the name of the parent account of this account.
    """
    ...

def leaf(account_name): # -> str | None:
    """Get the name of the leaf of this account.

    Args:
      account_name: A string, the name of the account whose leaf name to return.
    Returns:
      A string, the name of the leaf of the account.
    """
    ...

def sans_root(account_name): # -> str | None:
    """Get the name of the account without the root.

    For example, an input of 'Assets:BofA:Checking' will produce 'BofA:Checking'.

    Args:
      account_name: A string, the name of the account whose leaf name to return.
    Returns:
      A string, the name of the non-root portion of this account name.
    """
    ...

def root(num_components, account_name): # -> str:
    """Return the first few components of an account's name.

    Args:
      num_components: An integer, the number of components to return.
      account_name: A string, an account name.
    Returns:
      A string, the account root up to 'num_components' components.
    """
    ...

def has_component(account_name, component): # -> bool:
    """Return true if one of the account contains a given component.

    Args:
      account_name: A string, an account name.
      component: A string, a component of an account name. For instance,
        ``Food`` in ``Expenses:Food:Restaurant``. All components are considered.
    Returns:
      Boolean: true if the component is in the account. Note that a component
      name must be whole, that is ``NY`` is not in ``Expenses:Taxes:StateNY``.
    """
    ...

def commonprefix(accounts): # -> str:
    """Return the common prefix of a list of account names.

    Args:
      accounts: A sequence of account name strings.
    Returns:
      A string, the common parent account. If none, returns an empty string.
    """
    ...

def walk(root_directory): # -> Generator[tuple[Any, Any, list[Any], list[Any]], Any, None]:
    """A version of os.walk() which yields directories that are valid account names.

    This only yields directories that are accounts... it skips the other ones.
    For convenience, it also yields you the account's name.

    Args:
      root_directory: A string, the name of the root of the hierarchy to be walked.
    Yields:
      Tuples of (root, account-name, dirs, files), similar to os.walk().
    """
    ...

def parent_matcher(account_name): # -> Callable[..., Any]:
    """Build a predicate that returns whether an account is under the given one.

    Args:
      account_name: The name of the parent account we want to check for.
    Returns:
      A callable, which, when called, will return true if the given account is a
      child of ``account_name``.
    """
    ...

def parents(account_name): # -> Generator[Any | str, Any, None]:
    """A generator of the names of the parents of this account, including this account.

    Args:
      account_name: The name of the account we want to start iterating from.
    Returns:
      A generator of account name strings.
    """
    ...

class AccountTransformer:
    """Account name transformer.

    This is used to support Win... huh, filesystems and platforms which do not
    support colon characters.

    Attributes:
      rsep: A character string, the new separator to use in link names.
    """
    def __init__(self, rsep=...) -> None:
        ...
    
    def render(self, account_name):
        "Convert the account name to a transformed account name."
        ...
    
    def parse(self, transformed_name):
        "Convert the transform account name to an account name."
        ...
    

