"""
This type stub file was generated by pyright.
"""

"""Realization of specific lists of account postings into reports.

This code converts a list of entries into a tree of RealAccount nodes (which
stands for "realized accounts"). The RealAccount objects contain lists of
Posting instances instead of Transactions, or other entry types that are
attached to an account, such as a Balance or Note entry.

The interface of RealAccount corresponds to that of a regular Python dict, where
the keys are the names of the individual components of an account's name, and
the values are always other RealAccount instances. If you want to get an account
by long account name, there are helper functions in this module for this purpose
(see realization.get(), for instance). RealAccount instances also contain the
final balance of that account, resulting from its list of postings.

You should not build RealAccount trees yourself; instead, you should filter the
list of desired directives to display and call the realize() function with them.
"""
__copyright__ = ...
__license__ = ...
class RealAccount(dict):
    """A realized account, inserted in a tree, that contains the list of realized entries.

    Attributes:
      account: A string, the full name of the corresponding account.
      postings: A list of postings associated with this accounting (does not
        include the postings of children accounts).
      balance: The final balance of the list of postings associated with this account.
    """
    __slots__ = ...
    def __init__(self, account_name, *args, **kwargs) -> None:
        """Create a RealAccount instance.

        Args:
          account_name: a string, the name of the account. Maybe not be None.
        """
        ...
    
    def __setitem__(self, key, value): # -> None:
        """Prevent the setting of non-string or non-empty keys on this dict.

        Args:
          key: The dictionary key. Must be a string.
          value: The value, must be a RealAccount instance.
        Raises:
          KeyError: If the key is not a string, or is invalid.
          ValueError: If the value is not a RealAccount instance.
        """
        ...
    
    def copy(self): # -> Self:
        """Override dict.copy() to clone a RealAccount.

        This is only necessary to correctly implement the copy method.
        Otherwise, calling .copy() on a RealAccount instance invokes the base
        class' method, which return just a dict.

        Returns:
          A cloned instance of RealAccount, with all members shallow-copied.
        """
        ...
    
    def __eq__(self, other) -> bool:
        """Equality predicate. All attributes are compared.

        Args:
          other: Another instance of RealAccount.
        Returns:
          A boolean, True if the two real accounts are equal.
        """
        ...
    
    def __ne__(self, other) -> bool:
        """Not-equality predicate. See __eq__.

        Args:
          other: Another instance of RealAccount.
        Returns:
          A boolean, True if the two real accounts are not equal.
        """
        ...
    


def iter_children(real_account, leaf_only=...): # -> Generator[Any, Any, None]:
    """Iterate this account node and all its children, depth-first.

    Args:
      real_account: An instance of RealAccount.
      leaf_only: A boolean flag, true if we should yield only leaves.
    Yields:
      Instances of RealAccount, beginning with this account. The order is
      undetermined.
    """
    ...

def get(real_account, account_name, default=...): # -> None:
    """Fetch the subaccount name from the real_account node.

    Args:
      real_account: An instance of RealAccount, the parent node to look for
        children of.
      account_name: A string, the name of a possibly indirect child leaf
        found down the tree of 'real_account' nodes.
      default: The default value that should be returned if the child
        subaccount is not found.
    Returns:
      A RealAccount instance for the child, or the default value, if the child
      is not found.
    """
    ...

def get_or_create(real_account, account_name): # -> RealAccount:
    """Fetch the subaccount name from the real_account node.

    Args:
      real_account: An instance of RealAccount, the parent node to look for
        children of, or create under.
      account_name: A string, the name of the direct or indirect child leaf
        to get or create.
    Returns:
      A RealAccount instance for the child, or the default value, if the child
      is not found.
    """
    ...

def contains(real_account, account_name): # -> bool:
    """True if the given account node contains the subaccount name.

    Args:
      account_name: A string, the name of a direct or indirect subaccount of
        this node.
    Returns:
      A boolean, true the name is a child of this node.
    """
    ...

def realize(entries, min_accounts=..., compute_balance=...): # -> RealAccount:
    r"""Group entries by account, into a "tree" of realized accounts. RealAccount's
    are essentially containers for lists of postings and the final balance of
    each account, and may be non-leaf accounts (used strictly for organizing
    accounts into a hierarchy). This is then used to issue reports.

    The lists of postings in each account my be any of the entry types, except
    for Transaction, whereby Transaction entries are replaced by the specific
    Posting legs that belong to the account. Here's a simple diagram that
    summarizes this seemingly complex, but rather simple data structure:

       +-------------+ postings  +------+
       | RealAccount |---------->| Open |
       +-------------+           +------+
                                     |
                                     v
                              +------------+     +-------------+
                              | TxnPosting |---->| Transaction |
                              +------------+     +-------------+
                                     |      \                 \\\
                                     v       `\.__          +---------+
                                  +-----+         `-------->| Posting |
                                  | Pad |                   +---------+
                                  +-----+
                                     |
                                     v
                                +---------+
                                | Balance |
                                +---------+
                                     |
                                     v
                                 +-------+
                                 | Close |
                                 +-------+
                                     |
                                     .

    Args:
      entries: A list of directives.
      min_accounts: A list of strings, account names to ensure we create,
        regardless of whether there are postings on those accounts or not.
        This can be used to ensure the root accounts all exist.
      compute_balance: A boolean, true if we should compute the final
        balance on the realization.
    Returns:
      The root RealAccount instance.
    """
    ...

def postings_by_account(entries): # -> defaultdict[Any, list[Any]]:
    """Create lists of postings and balances by account.

    This routine aggregates postings and entries grouping them by account name.
    The resulting lists contain postings in-lieu of Transaction directives, but
    the other directives are stored as entries. This yields a list of postings
    or other entries by account. All references to accounts are taken into
    account.

    Args:
      entries: A list of directives.
    Returns:
       A mapping of account name to list of TxnPosting instances or
       non-Transaction directives, sorted in the same order as the entries.
    """
    ...

def filter(real_account, predicate): # -> RealAccount | None:
    """Filter a RealAccount tree of nodes by the predicate.

    This function visits the tree and applies the predicate on each node. It
    returns a partial clone of RealAccount whereby on each node
    - either the predicate is true, or
    - for at least one child of the node the predicate is true.
    All the leaves have the predicate be true.

    Args:
      real_account: An instance of RealAccount.
      predicate: A callable/function which accepts a real_account and returns
        a boolean. If the function returns True, the node is kept.
    Returns:
      A shallow clone of RealAccount is always returned.
    """
    ...

def get_postings(real_account): # -> list[Any]:
    """Return a sorted list a RealAccount's postings and children.

    Args:
      real_account: An instance of RealAccount.
    Returns:
      A list of Posting or directories.
    """
    ...

def iterate_with_balance(txn_postings): # -> Generator[tuple[Any, Any, Inventory, Inventory], Any, None]:
    """Iterate over the entries, accumulating the running balance.

    For each entry, this yields tuples of the form:

      (entry, postings, change, balance)

    entry: This is the directive for this line. If the list contained Posting
      instance, this yields the corresponding Transaction object.
    postings: A list of postings on this entry that affect the balance. Only the
      postings encountered in the input list are included; only those affect the
      balance. If 'entry' is not a Transaction directive, this should always be
      an empty list. We preserve the original ordering of the postings as they
      appear in the input list.
    change: An Inventory object that reflects the total change due to the
      postings from this entry that appear in the list. For example, if a
      Transaction has three postings and two are in the input list, the sum of
      the two postings will be in the 'change' Inventory object. However, the
      position for the transactions' third posting--the one not included in the
      input list--will not be in this inventory.
    balance: An Inventory object that reflects the balance *after* adding the
      'change' inventory due to this entry's transaction. The 'balance' yielded
      is never None, even for entries that do not affect the balance, that is,
      with an empty 'change' inventory. It's up to the caller, the one rendering
      the entry, to decide whether to render this entry's change for a
      particular entry type.

    Note that if the input list of postings-or-entries is not in sorted date
    order, two postings for the same entry appearing twice with a different date
    in between will cause the entry appear twice. This is correct behavior, and
    it is expected that in practice this should never happen anyway, because the
    list of postings or entries should always be sorted. This method attempts to
    detect this and raises an assertion if this is seen.

    Args:
      txn_postings: A list of postings or directive instances.
        Postings affect the balance; other entries do not.
    Yields:
      Tuples of (entry, postings, change, balance) as described above.
    """
    ...

def compute_balance(real_account, leaf_only=...): # -> Any:
    """Compute the total balance of this account and all its subaccounts.

    Args:
      real_account: A RealAccount instance.
      leaf_only: A boolean flag, true if we should yield only leaves.
    Returns:
      An Inventory.
    """
    ...

def find_last_active_posting(txn_postings): # -> TxnPosting | None:
    """Look at the end of the list of postings, and find the last
    posting or entry that is not an automatically added directive.
    Note that if the account is closed, the last posting is assumed
    to be a Close directive (this is the case if the input is valid
    and checks without errors.

    Args:
      txn_postings: a list of postings or entries.
    Returns:
      An entry, or None, if the input list was empty.
    """
    ...

def index_key(sequence, value, key, cmp): # -> int | None:
    """Find the index of the first element in 'sequence' which is equal to 'value'.
    If 'key' is specified, the value compared to the value returned by this
    function. If the value is not found, return None.

    Args:
      sequence: The sequence to search.
      value: The value to search for.
      key: A predicate to call to obtain the value to compare against.
      cmp: A comparison predicate.
    Returns:
      The index of the first element found, or None, if the element was not found.
    """
    ...

def dump(root_account): # -> list[Any] | list[tuple[str, str, Any]]:
    """Convert a RealAccount node to a line of lines.

    Note: this is not meant to be used to produce text reports; the reporting
    code should produce an intermediate object that contains the structure of
    it, which can then be rendered to ASCII, HTML or CSV formats. This is
    intended as a convenient little function for dumping trees of data for
    debugging purposes.

    Args:
      root_account: A RealAccount instance.
    Returns:
      A list of tuples of (first_line, continuation_line, real_account) where
        first_line: A string, the first line to render, which includes the
          account name.
        continuation_line: A string, further line to render if necessary.
        real_account: The RealAccount instance which corresponds to this
          line.
    """
    ...

PREFIX_CHILD_1 = ...
PREFIX_CHILD_C = ...
PREFIX_LEAF_1 = ...
PREFIX_LEAF_C = ...
def dump_balances(real_root, dformat, at_cost=..., fullnames=..., file=...): # -> str | None:
    """Dump a realization tree with balances.

    Args:
      real_root: An instance of RealAccount.
      dformat: An instance of DisplayFormatter to format the numbers with.
      at_cost: A boolean, if true, render the values at cost.
      fullnames: A boolean, if true, don't render a tree of accounts and
        render the full account names.
      file: A file object to dump the output to. If not specified, we
        return the output as a string.
    Returns:
      A string, the rendered tree, or nothing, if 'file' was provided.
    """
    ...

def compute_postings_balance(txn_postings): # -> Inventory:
    """Compute the balance of a list of Postings's or TxnPosting's positions.

    Args:
      postings: A list of Posting instances and other directives (which are
        skipped).
    Returns:
      An Inventory.
    """
    ...

