"""
This module demonstrates key concepts including positional/keyword arguments, default parameters,
*args and **kwargs, closures, yield vs return, and LEGB scope resolution.

"""

# -----------------------------
# 1. Function Definitions: Positional vs Keyword Arguments
# -----------------------------

def greet(name, age):
    """
    Greets a user with their name and age.
    Demonstrates positional and keyword argument usage.
    """
    return f"Hello {name}, you are {age} years old."

print(greet("Alice", 30))               # Positional
print(greet(age=25, name="Bob"))        # Keyword


# -----------------------------
# 2. *args and **kwargs: Dynamic Arguments
# -----------------------------

def demo_args_kwargs(*args, **kwargs):
    """
    Demonstrates the use of *args (tuple of extra positional args) and
    **kwargs (dict of extra keyword args).
    """
    print("Positional (args):", args)
    print("Keyword (kwargs):", kwargs)

# demo_args_kwargs(1, 2, 3, x=10, y=20)


# -----------------------------
# 3. Default Parameters and Pitfall
# -----------------------------

def add_to_list(value, my_list=None):
    """
    Shows safe handling of mutable default arguments.

    Using None prevents shared list across function calls.
    """
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# -----------------------------
# 4. Return vs Yield: Generators vs Functions
# -----------------------------

def use_return():
    """
    Regular function that returns all values at once.
    """
    return [1, 2, 3]

def use_yield():
    """
    Generator function yielding values one by one.
    Saves memory for large data streams.
    """
    yield 1
    yield 2
    yield 3


# -----------------------------
# 5. Closures: Retaining State
# -----------------------------

def outer_closure(x):
    """
    Closure: Inner function retains access to outer variable 'x'.
    Used in decorators, factories, caching, etc.
    """
    def inner(y):
        return x + y
    return inner

# add_5 = outer_closure(5)
# print(add_5(10))  # 15


# -----------------------------
# 6. Scope: LEGB Rule
# -----------------------------

x = "global"

def outer_scope():
    x = "enclosing"

    def inner_scope():
        x = "local"
        print("Scope example (local):", x)

    inner_scope()
    print("Scope example (enclosing):", x)

print("Scope example (global):", x)
outer_scope()


# -----------------------------
# 7. nonlocal and global Keywords
# -----------------------------

def counter():
    """
    Demonstrates use of nonlocal to modify enclosing scope variable.
    """
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# inc = counter()
# print(inc())  # 1
# print(inc())  # 2


def global_demo():
    """
    Demonstrates use of global to modify module-level variable.
    """
    global x
    x = "modified global"

# global_demo()
# print(x)  # "modified global"
