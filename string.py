# string.py

"""
Masterclass: Everything You Should Know About Python Strings
Written for serious Python developers
"""

# 1️⃣ String Declaration
empty = ""
non_empty = "Hello, Python!"
multiline = """This is
a multiline string."""

# 2️⃣ String Indexing & Slicing
s = "Python"
first = s[0]        # 'P'
last = s[-1]        # 'n'
sub = s[1:4]        # 'yth'
reverse = s[::-1]   # 'nohtyP'

# 3️⃣ String Immutability
try:
    s[0] = 'J'  # ❌ Error: strings are immutable
except TypeError as e:
    print("Strings are immutable:", e)

# 4️⃣ Concatenation & Repetition
a = "Hello"
b = "World"
concat = a + " " + b      # 'Hello World'
repeat = a * 3            # 'HelloHelloHello'

# 5️⃣ Useful Built-in Methods
text = "  Python is powerful!  "

print(text.strip())         # Removes leading/trailing whitespace
print(text.lower())         # Lowercase
print(text.upper())         # Uppercase
print(text.title())         # Title Case
print(text.replace("Python", "Java"))  # Replace substrings
print(text.startswith("  Py"))         # True
print(text.endswith("!  "))            # True
print("is" in text)         # Membership test
print(text.count("o"))     # Count occurrences
print(text.find("power"))  # Index of substring or -1
print(text.split())        # Split by whitespace
print("-".join(["a", "b", "c"]))  # Join list with separator

# 6️⃣ f-Strings and Formatting
name = "Shreeharsh"
score = 99.123456

print(f"Hi, {name}! Your score is {score:.2f}")  # f-String formatting
print("Hello {}, your score is {:.1f}".format(name, score))  # str.format
print("%s scored %.2f marks" % (name, score))  # Old-style formatting

# 7️⃣ Escape Sequences
escape_demo = "Line1\nLine2\tTabbed\\Backslash\'Quote\""

# 8️⃣ Raw Strings (useful for regex and Windows paths)
path = r"C:\Users\Shreeharsh\Documents"
regex = r"\d{3}-\d{2}-\d{4}"  # No need to double escape

# 9️⃣ Unicode and Encoding
unicode_str = "こんにちは"
encoded = unicode_str.encode('utf-8')
decoded = encoded.decode('utf-8')

# 🔟 isX Methods (string classification)
print("abc123".isalnum())   # True
print("abc".isalpha())      # True
print("123".isdigit())      # True
print("   ".isspace())      # True
print("Python".isidentifier())  # True
print("Hello".istitle())    # False
print("HELLO".isupper())    # True

# 🔁 String Iteration
for char in "Loop":
    print(char, end=' ')  # Output: L o o p

# 🧠 Advanced: String Interning
a = "interned"
b = "interned"
print(a is b)  # True — Python interns short strings
x = "".join(["in", "terned"])
print(a == x, a is x)  # True, False — content same, object not interned

# 🧪 Testing and Assertion
assert "python".capitalize() == "Python"
assert "data science".title() == "Data Science"

# 🧹 Cleanup
del s, a, b, name, score, text

print("✅ All string operations demonstrated successfully!")
