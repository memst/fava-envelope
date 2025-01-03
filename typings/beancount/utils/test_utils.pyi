"""
This type stub file was generated by pyright.
"""

import unittest
import contextlib

"""Support utilities for testing scripts.
"""
__copyright__ = ...
__license__ = ...
get_test_port = ...
def nottest(func):
    "Make the given function not testable."
    ...

def find_repository_root(filename=...): # -> str | Any:
    """Return the path to the repository root.

    Args:
      filename: A string, the name of a file within the repository.
    Returns:
      A string, the root directory.
    """
    ...

def find_python_lib(): # -> str:
    """Return the path to the root of the Python libraries.

    Returns:
      A string, the root directory.
    """
    ...

def subprocess_env(): # -> dict[str, str]:
    """Return a dict to use as environment for running subprocesses.

    Returns:
      A string, the root directory.
    """
    ...

def run_with_args(function, args, runner_file=...):
    """Run the given function with sys.argv set to argv. The first argument is
    automatically inferred to be where the function object was defined. sys.argv
    is restored after the function is called.

    Args:
      function: A function object to call with no arguments.
      argv: A list of arguments, excluding the script name, to be temporarily
        set on sys.argv.
      runner_file: An optional name of the top-level file being run.
    Returns:
      The return value of the function run.
    """
    ...

def call_command(command): # -> tuple[int | Any, str, str]:
    """Run the script with a subprocess.

    Args:
      script_args: A list of strings, the arguments to the subprocess,
        including the script name.
    Returns:
      A triplet of (return code integer, stdout ext, stderr text).
    """
    ...

@contextlib.contextmanager
def tempdir(delete=..., **kw): # -> Generator[str, Any, None]:
    """A context manager that creates a temporary directory and deletes its
    contents unconditionally once done.

    Args:
      delete: A boolean, true if we want to delete the directory after running.
      **kw: Keyword arguments for mkdtemp.
    Yields:
      A string, the name of the temporary directory created.
    """
    ...

def create_temporary_files(root, contents_map): # -> None:
    """Create a number of temporary files under 'root'.

    This routine is used to initialize the contents of multiple files under a
    temporary directory.

    Args:
      root: A string, the name of the directory under which to create the files.
      contents_map: A dict of relative filenames to their contents. The content
        strings will be automatically dedented for convenience. In addition, the
        string 'ROOT' in the contents will be automatically replaced by the root
        directory name.
    """
    ...

def capture(*attributes): # -> _GeneratorContextManager[Any | list[Any]]:
    """A context manager that captures what's printed to stdout.

    Args:
      *attributes: A tuple of strings, the name of the sys attributes to override
        with StringIO instances.
    Yields:
      A StringIO string accumulator.
    """
    ...

@contextlib.contextmanager
def patch(obj, attributes, replacement_type): # -> Generator[Any | list[Any], Any, None]:
    """A context manager that temporarily patches an object's attributes.

    All attributes in 'attributes' are saved and replaced by new instances
    of type 'replacement_type'.

    Args:
      obj: The object to patch up.
      attributes: A string or a sequence of strings, the names of attributes to replace.
      replacement_type: A callable to build replacement objects.
    Yields:
      An instance of a list of sequences of 'replacement_type'.
    """
    ...

def docfile(function, **kwargs): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """A decorator that write the function's docstring to a temporary file
    and calls the decorated function with the temporary filename.  This is
    useful for writing tests.

    Args:
      function: A function to decorate.
    Returns:
      The decorated function.
    """
    ...

def docfile_extra(**kwargs): # -> partial[_Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]]:
    """
    A decorator identical to @docfile,
    but it also takes kwargs for the temporary file,
    Kwargs:
      e.g. buffering, encoding, newline, dir, prefix, and suffix.
    Returns:
      docfile
    """
    ...

def search_words(words, line): # -> Match[str] | None:
    """Search for a sequence of words in a line.

    Args:
      words: A list of strings, the words to look for, or a space-separated string.
      line: A string, the line to search into.
    Returns:
      A MatchObject, or None.
    """
    ...

class TestTempdirMixin:
    def setUp(self): # -> None:
        ...
    
    def tearDown(self): # -> None:
        ...
    


class TmpFilesTestBase(unittest.TestCase):
    """A test utility base class that creates and cleans up a directory hierarchy.
    This convenience is useful for testing functions that work on files, such as the
    documents tests, or the accounts walk.
    """
    TEST_DOCUMENTS = ...
    def setUp(self): # -> None:
        ...
    
    def tearDown(self): # -> None:
        ...
    
    @staticmethod
    def create_file_hierarchy(test_files, subdir=...): # -> tuple[str, str]:
        """A test utility that creates a hierarchy of files.

        Args:
          test_files: A list of strings, relative filenames to a temporary root
            directory. If the filename ends with a '/', we create a directory;
            otherwise, we create a regular file.
          subdir: A string, the subdirectory name under the temporary directory
            location, to create the hierarchy under.
        Returns:
          A pair of strings, the temporary directory, and the subdirectory under
            that which hosts the root of the tree.
        """
        ...
    


class TestCase(unittest.TestCase):
    def assertLines(self, text1, text2, message=...): # -> None:
        """Compare the lines of text1 and text2, ignoring whitespace.

        Args:
          text1: A string, the expected text.
          text2: A string, the actual text.
          message: An optional string message in case the assertion fails.
        Raises:
          AssertionError: If the exception fails.
        """
        ...
    
    @contextlib.contextmanager
    def assertOutput(self, expected_text): # -> Generator[Any | list[Any], Any, None]:
        """Expect text printed to stdout.

        Args:
          expected_text: A string, the text that should have been printed to stdout.
        Raises:
          AssertionError: If the text differs.
        """
        ...
    


@contextlib.contextmanager
def skipIfRaises(*exc_types): # -> Generator[None, Any, None]:
    """A context manager (or decorator) that skips a test if an exception is raised.

    Args:
      exc_type
    Yields:
      Nothing, for you to execute the function code.
    Raises:
      SkipTest: if the test raised the expected exception.
    """
    ...

def make_failing_importer(*removed_module_names): # -> Callable[..., Any]:
    """Make an importer that raise an ImportError for some modules.

    Use it like this:

      @mock.patch('builtins.__import__', make_failing_importer('setuptools'))
      def test_...

    Args:
      removed_module_name: The name of the module import that should raise an exception.
    Returns:
      A decorated test decorator.
    """
    ...

@contextlib.contextmanager
def environ(varname, newvalue): # -> Generator[None, Any, None]:
    """A context manager which pushes varname's value and restores it later.

    Args:
      varname: A string, the environ variable name.
      newvalue: A string, the desired value.
    """
    ...

RCall = ...
def record(fun): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """Decorates the function to intercept and record all calls and return values.

    Args:
      fun: A callable to be decorated.
    Returns:
      A wrapper function with a .calls attribute, a list of RCall instances.
    """
    ...

def remove_alt_csv_path(): # -> None:
    """Remove folder containing the csv module from the import path.

    For some strange reason Bazel insists on inserting the local directory of
    the file on sys.path and 'import csv' will fail to resolve to the global
    module. TODO(blais): In the next version, renmame 'csv' to a different name.
    """
    ...

