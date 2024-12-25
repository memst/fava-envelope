"""
This type stub file was generated by pyright.
"""

import contextlib

"""File utilities.
"""
__copyright__ = ...
__license__ = ...
def find_files(fords, ignore_dirs=..., ignore_files=...): # -> Generator[str | Any, Any, None]:
    """Enumerate the files under the given directories, stably.

    Invalid file or directory names will be logged to the error log.

    Args:
      fords: A list of strings, file or directory names.
      ignore_dirs: A list of strings, filenames or directories to be ignored.
    Yields:
      Strings, full filenames from the given roots.
    """
    ...

def guess_file_format(filename, default=...): # -> Literal['text', 'csv', 'html'] | None:
    """Guess the file format from the filename.

    Args:
      filename: A string, the name of the file. This can be None.
    Returns:
      A string, the extension of the format, without a leading period.
    """
    ...

def path_greedy_split(filename): # -> tuple[Any, Any | None]:
    """Split a path, returning the longest possible extension.

    Args:
      filename: A string, the filename to split.
    Returns:
      A pair of basename, extension (which includes the leading period).
    """
    ...

def touch_file(filename, *otherfiles): # -> None:
    """Touch a file and wait until its timestamp has been changed.

    Args:
      filename: A string path, the name of the file to touch.
      otherfiles: A list of other files to ensure the timestamp is beyond of.
    """
    ...

@contextlib.contextmanager
def chdir(directory): # -> Generator[str, Any, None]:
    """Temporarily chdir to the given directory.

    Args:
      directory: The directory to switch do.
    Returns:
      A context manager which restores the cwd after running.
    """
    ...

