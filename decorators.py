from functools import wraps


def log(func):
    """
        A decorator that logs the function name before calling it.

        This decorator uses `functools.wraps()` to preserve the metadata
        (such as function name, docstring, and other attributes) of the
        original function being decorated.

        Why is `@wraps` important?
        --------------------------
        When you write decorators without `@wraps`, the function returned
        by the decorator (usually a `wrapper`) replaces the original function.
        As a result:
            - `__name__` becomes "wrapper"
            - `__doc__` becomes None
            - `help()` and introspection tools stop working properly
            - Testing, debugging, logging become harder

        By using `@wraps(func)`, the wrapper function inherits:
            - `__name__` → correct name (like 'greet')
            - `__doc__`  → original docstring
            - Other metadata like annotations, module info, etc.

        Example
        -------
        >>> @log
        ... def greet(name):
        ...     \"\"\"Greet the user by name.\"\"\"
        ...     print(f"Hello, {name}")
        ...
        >>> greet("Shreeharsh")
        Calling: greet
        Hello, Shreeharsh
        >>> print(greet.__name__)
        greet
        >>> print(greet.__doc__)
        Greet the user by name.

        Parameters
        ----------
        func : function
            The original function to be wrapped.

        Returns
        -------
        function
            The wrapped version of `func` with logging and preserved metadata.
        """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name):
    print(f"Hello, {name}")

greet("Shreeharsh") # Calling: greet Hello, Shreeharsh

print(greet.__name__)
