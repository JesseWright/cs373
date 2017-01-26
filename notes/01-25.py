# -----------
# Wed, 25 Jan
# -----------

"""
Unit tests represent white-box testing.
Acceptance tests represent black-box testing.

Collatz.py represents the kernel of the solution.
RunCollatz.py is the run harness.
TestCollatz.py is the test harness.

Combine Collatz.py and RunCollatz.py into a separate file to then send to HackerRank.

Collatz.py needs to abstract where input is coming from and where output is going to.

sys.stdin and sys.stdout are of type TextIOWrapper.
StringIO includes TextIOWrapper's API.

So, RunCollatz.py provides sys.stdin and sys.stdout, and
TestCollatz.py provides two StringIO objects.

Java's constructors and methods can be overloaded. It just requires different types of argument or a different number of arguments.

Python doesn't have overloading. But, it does have default arguments.

So,
"""

r = StringIO("abc")
w = StringIO()

"""
are the same constructor.

StringIO.getvalue() retrieves the string that is inside of the StringIO object.

The solution to the Collatz problem is best structured as a read-eval-print-loop (REPL).

You can use "_" as a variable name, when you don't need the value of the variable.
"""
