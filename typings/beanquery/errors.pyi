"""
This type stub file was generated by pyright.
"""

"""
Exceptions hierarchy defined by the DB-API:

    Exception
      Warning
      Error
        InterfaceError
        DatabaseError
          DataError
          OperationalError
          IntegrityError
          InternalError
          ProgrammingError
          NotSupportedError
"""
class Warning(Exception):
    """Exception raised for important warnings."""
    __module__ = ...


class Error(Exception):
    """Base exception for all errors."""
    __module__ = ...


class InterfaceError(Error):
    """An error related to the database interface rather than the database itself."""
    __module__ = ...


class DatabaseError(Error):
    """Exception raised for errors that are related to the database."""
    __module__ = ...


class DataError(DatabaseError):
    """An error caused by problems with the processed data."""
    __module__ = ...


class OperationalError(DatabaseError):
    """An error related to the database's operation."""
    __module__ = ...


class IntegrityError(DatabaseError):
    """An error caused when the relational integrity of the database is affected."""
    __module__ = ...


class InternalError(DatabaseError):
    """An error generated when the database encounters an internal error."""
    __module__ = ...


class ProgrammingError(DatabaseError):
    """Exception raised for programming errors."""
    __module__ = ...


class NotSupportedError(DatabaseError):
    """A method or database API was used which is not supported by the database."""
    __module__ = ...


