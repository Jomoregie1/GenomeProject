class InvalidDelimiterError(Exception):
    """
    Custom exception raised when an invalid delimiter is detected in the input data.

    This exception should be raised when the input file does not use the expected delimiter,
    such as a tab character or a specific pattern of space-separated values. It can be caught
    and handled accordingly to provide meaningful error messages to the user or for debugging
    purposes.
    """
    pass
