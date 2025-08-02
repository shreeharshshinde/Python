from collections import namedtuple

"""
collections_module_demo.py

A comprehensive guide and demonstration of Python's built-in `collections` module.

The `collections` module is part of Python's standard library and provides specialized 
container data types that are alternatives to Python's built-in types like `list`, 
`tuple`, and `dict`. These are optimized for specific use-cases and add powerful 
functionality for real-world software and algorithmic design.

This module demonstrates the usage and purpose of each major class available in 
the `collections` module with annotated examples.

Included Components:
--------------------

1. namedtuple   - Factory function to create tuple subclasses with named fields.
2. deque        - Double-ended queue for fast appends and pops from both ends.
3. Counter      - Dictionary subclass for counting hashable objects.
4. defaultdict  - Dictionary subclass that provides default values for missing keys.
5. OrderedDict  - Dictionary that remembers the insertion order of keys (useful in < Py3.7).
6. ChainMap     - Groups multiple dictionaries into a single, viewable mapping.
7. UserDict     - Wrapper class around dictionaries for easier subclassing.
8. (Bonus) UserList & UserString - For customizing list/string behavior.

Each component is illustrated with:
- Use-case driven examples
- Relevant method usages
- Interview-level insights

Ideal for:
----------
✔ Interview preparation  
✔ Clean, maintainable Python code  
✔ High-performance data handling  
✔ Intermediate to advanced Python developers

Author: Your Name
License: MIT
"""

"""
1. Namedtuple
"""
Point = namedtuple("Point", "x y")

def create_point(x, y):
    """
    Creates a 2D point using namedtuple for better readability and maintainability.

    Unlike regular tuples where access is index-based, namedtuples allow
    accessing values via field names like `.x` and `.y`, making the code
    more self-explanatory and less error-prone.

    Namedtuples are immutable, meaning their values cannot be changed after creation.

    Parameters:
    -----------
    x : int or float
        X-coordinate of the point.
    y : int or float
        Y-coordinate of the point.

    Returns:
    --------
    Point
        A namedtuple instance with fields 'x' and 'y'.
    """
    return Point(x, y)

p = create_point(5, 7)
print(p.x, p.y)
print(p._asdict())       # Converts to OrderedDict
print(p._replace(x=10))  # Returns a new Point with x modified

"""
2. Deque
"""

from collections import deque

def demo_deque_operations():
    """
    Demonstrates how `deque` (double-ended queue) allows fast insertions and deletions
    from both ends in O(1) time, unlike list which has O(n) complexity for insertions
    or deletions from the start.

    Deque is ideal for:
    - Queues
    - Stacks
    - Sliding window algorithms

    Returns:
    --------
    list
        A deque after a series of append and pop operations.
    """
    d = deque([1, 2, 3])
    d.append(4)         # [1, 2, 3, 4]
    d.appendleft(0)     # [0, 1, 2, 3, 4]
    d.pop()             # [0, 1, 2, 3]
    d.popleft()         # [1, 2, 3]
    return list(d)

print(demo_deque_operations())

"""
3. Counter
"""
from collections import Counter

def analyze_frequencies(data):
    """
    Uses `Counter` to count the frequency of elements in any iterable.

    Counter is a subclass of dict specifically designed for counting hashable elements.
    It returns a dictionary-like object where keys are elements, and values are counts.

    Parameters:
    -----------
    data : iterable
        A string, list, or any iterable containing hashable items.

    Returns:
    --------
    Counter
        A mapping from elements to their frequencies.
    """
    c = Counter(data)
    print("Most Common:", c.most_common(2))
    print("Elements > 1:", [item for item, count in c.items() if count > 1])
    return c

print(analyze_frequencies("abracadabra"))

"""
4. DefaultDict
"""
from collections import defaultdict

def build_index(pairs):
    """
    Groups values by their keys using `defaultdict`.

    defaultdict takes a default factory (like list, int, or set) and automatically
    initializes missing keys with a default value, avoiding KeyErrors.

    Ideal for grouping, frequency mapping, and building indexes.

    Parameters:
    -----------
    pairs : list of tuples
        A list of (key, value) pairs to group.

    Returns:
    --------
    dict
        A regular dictionary with grouped values.
    """
    grouped = defaultdict(list)
    for k, v in pairs:
        grouped[k].append(v)
    return dict(grouped)

data = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
print(build_index(data))

"""
5. OrderedDict
"""
from collections import OrderedDict

def ordered_dict_example():
    """
    Demonstrates OrderedDict, which preserves the insertion order of keys.

    While Python 3.7+ dicts preserve insertion order by default, OrderedDict
    also supports key reordering operations like `move_to_end`.

    Useful when key order matters in serialization or algorithmic steps.

    Returns:
    --------
    OrderedDict
        An ordered dictionary after key movements.
    """
    od = OrderedDict()
    od['first'] = 1
    od['second'] = 2
    od['third'] = 3

    od.move_to_end('first')  # Push to end
    od.move_to_end('third', last=False)  # Bring to front
    return od

print(ordered_dict_example())


"""
6. ChainMap
"""
from collections import ChainMap

def combine_configs(user, default):
    """
    Combines multiple dictionaries using ChainMap, searching in the order they’re added.

    ChainMap enables treating multiple dicts as a single mapping.
    Lookup is done from left to right; writes always go to the first mapping.

    Parameters:
    -----------
    user : dict
        User-specified config (overrides).
    default : dict
        Default config.

    Returns:
    --------
    ChainMap
        A merged view of both dictionaries.
    """
    config = ChainMap(user, default)
    return config

defaults = {"theme": "light", "language": "English"}
overrides = {"theme": "dark"}

print(combine_configs(overrides, defaults))  # {'theme': 'dark', 'language': 'English'}


"""
7. UserDict
"""
from collections import UserDict

class LoggingDict(UserDict):
    """
    Custom dict that logs every key assignment.

    Useful for debugging, caching, or tracking changes in mutable mappings.
    UserDict wraps a regular dictionary but provides a clean way to override behavior.
    """

    def __setitem__(self, key, value):
        print(f"Setting {key} = {value}")
        super().__setitem__(key, value)

d = LoggingDict()
d["foo"] = "bar"  # Setting foo = bar
d["x"] = 42       # Setting x = 42

