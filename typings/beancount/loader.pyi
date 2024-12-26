"""
This type stub file was generated by pyright.
"""

from typing import Optional

"""Loader code. This is the main entry point to load up a file.
"""
__copyright__ = ...
__license__ = ...
LoadError = ...
DEFAULT_PLUGINS_PRE = ...
DEFAULT_PLUGINS_POST = ...
RENAMED_MODULES = ...
PICKLE_CACHE_FILENAME = ...
PICKLE_CACHE_THRESHOLD = ...
def load_file(filename, log_timings=..., log_errors=..., extra_validations=..., encoding=...): # -> tuple[Any, list[Any] | Any, dict[Any, Any] | Any]:
    """Open a Beancount input file, parse it, run transformations and validate.

    Args:
      filename: The name of the file to be parsed.
      log_timings: A file object or function to write timings to,
        or None, if it should remain quiet.
      log_errors: A file object or function to write errors to,
        or None, if it should remain quiet.
      extra_validations: A list of extra validation functions to run after loading
        this list of entries.
      encoding: A string or None, the encoding to decode the input filename with.
    Returns:
      A triple of (entries, errors, options_map) where "entries" is a date-sorted
      list of entries from the file, "errors" a list of error objects generated
      while parsing and validating the file, and "options_map", a dict of the
      options parsed from the file.
    """
    ...

def load_encrypted_file(filename, log_timings=..., log_errors=..., extra_validations=..., dedent=..., encoding=...): # -> tuple[Any, list[Any], dict[Any, Any]]:
    """Load an encrypted Beancount input file.

    Args:
      filename: The name of an encrypted file to be parsed.
      log_timings: See load_string().
      log_errors: See load_string().
      extra_validations: See load_string().
      dedent: See load_string().
      encoding: See load_string().
    Returns:
      A triple of (entries, errors, options_map) where "entries" is a date-sorted
      list of entries from the file, "errors" a list of error objects generated
      while parsing and validating the file, and "options_map", a dict of the
      options parsed from the file.
    """
    ...

def get_cache_filename(pattern: str, filename: str) -> str:
    """Compute the cache filename from a given pattern and the top-level filename.

    Args:
      pattern: A cache filename or pattern. If the pattern contains '{filename}' this
        will get replaced by the top-level filename. This may be absolute or relative.
      filename: The top-level filename.
    Returns:
      The resolved cache filename.
    """
    ...

def pickle_cache_function(cache_getter, time_threshold, function): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """Decorate a loader function to make it loads its result from a pickle cache.

    This considers the first argument as a top-level filename and assumes the
    function to be cached returns an (entries, errors, options_map) triple. We
    use the 'include' option value in order to check whether any of the included
    files has changed. It's essentially a special case for an on-disk memoizer.
    If any of the included files are more recent than the cache, the function is
    recomputed and the cache refreshed.

    Args:
      cache_getter: A function of one argument, the top-level filename, which
        will return the name of the corresponding cache file.
      time_threshold: A float, the number of seconds below which we don't bother
        caching.
      function: A function object to decorate for caching.
    Returns:
      A decorated function which will pull its result from a cache file if
      it is available.
    """
    ...

def delete_cache_function(cache_getter, function): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """A wrapper that removes the cached filename.

    Args:
      cache_getter: A function of one argument, the top-level filename, which
        will return the name of the corresponding cache file.
      function: A function object to decorate for caching.
    Returns:
      A decorated function which will delete the cached filename, if it exists.
    """
    ...

def needs_refresh(options_map): # -> Literal[True]:
    """Predicate that returns true if at least one of the input files may have changed.

    Args:
      options_map: An options dict as per the parser.
      mtime: A modified time, to check if it covers the include files in the options_map.
    Returns:
      A boolean, true if the input is obsoleted by changes in the input files.
    """
    ...

def compute_input_hash(filenames): # -> str:
    """Compute a hash of the input data.

    Args:
      filenames: A list of input files. Order is not relevant.
    """
    ...

def load_string(string, log_timings=..., log_errors=..., extra_validations=..., dedent=..., encoding=...): # -> tuple[Any, list[Any], dict[Any, Any]]:
    """Open a Beancount input string, parse it, run transformations and validate.

    Args:
      string: A Beancount input string.
      log_timings: A file object or function to write timings to,
        or None, if it should remain quiet.
      log_errors: A file object or function to write errors to,
        or None, if it should remain quiet.
      extra_validations: A list of extra validation functions to run after loading
        this list of entries.
      dedent: A boolean, if set, remove the whitespace in front of the lines.
      encoding: A string or None, the encoding to decode the input string with.
    Returns:
      A triple of (entries, errors, option_map) where "entries" is a date-sorted
      list of entries from the string, "errors" a list of error objects
      generated while parsing and validating the string, and "options_map", a
      dict of the options parsed from the string.
    """
    ...

def aggregate_options_map(options_map, src_options_map): # -> None:
    """Aggregate some of the attributes of options map.

    Args:
      options_map: The target map in which we want to aggregate attributes.
        Note: This value is mutated in-place.
      src_options_map: A source map whose values we'd like to see aggregated.
    """
    ...

def run_transformations(entries, parse_errors, options_map, log_timings): # -> tuple[Any, list[Any]]:
    """Run the various transformations on the entries.

    This is where entries are being synthesized, checked, plugins are run, etc.

    Args:
      entries: A list of directives as read from the parser.
      parse_errors: A list of errors so far.
      options_map: An options dict as read from the parser.
      log_timings: A function to write timing log entries to, or None, if it
        should be quiet.
    Returns:
      A list of modified entries, and a list of errors, also possibly modified.
    """
    ...

def combine_plugins(*plugin_modules): # -> list[Any]:
    """Combine the plugins from the given plugin modules.

    This is used to create plugins of plugins.
    Args:
      *plugins_modules: A sequence of module objects.
    Returns:
      A list that can be assigned to the new module's __plugins__ attribute.
    """
    ...

def load_doc(expect_errors=...): # -> Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]]:
    """A factory of decorators that loads the docstring and calls the function with entries.

    This is an incredibly convenient tool to write lots of tests. Write a
    unittest using the standard TestCase class and put the input entries in the
    function's docstring.

    Args:
      expect_errors: A boolean or None, with the following semantics,
        True: Expect errors and fail if there are none.
        False: Expect no errors and fail if there are some.
        None: Do nothing, no check.
    Returns:
      A wrapped method that accepts a single 'self' argument.
    """
    ...

def initialize(use_cache: bool, cache_filename: Optional[str] = ...): # -> None:
    """Initialize the loader."""
    ...
