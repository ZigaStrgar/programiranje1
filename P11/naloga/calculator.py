# Ocena 6 / Grade 6
valid_operators = {"NOT", "AND", "OR", "RSHIFT", "LSHIFT", "SET"}


def to_number(s):
    """Convert string to int if possible, else return the original string.

    `to_number('42')` returns 42, while `to_number('x')` returns 'x'.

    Args:
        s (str): string that is converted to a number

    Returns:
        int: if the argument contains a number; `to_number('42')` return `42`
        str: otherwise; `to_number('x')` return `'x'`
    """
    return int(s) if s.isdigit() else s


def parse(s):
    """Parse a string with expression into tuple `(name, operation, arguments)`.

    Args:
        s (str): expression

    Returns:
        tuple: expression parsed into `(name, operation, arguments)`

    See documentation for function :func:`read` for examples of expressions.

    The operation can be unary SET or NOT, or binary AND, OR, LSHIFT or RSHIFT.
    Note that SET is not spelled out in the input string; see the examples
    below. The last element, `arguments` is itself a tuple of arguments; that
    is, a tuple with 1 or 2 elements. Numeric arguments are converted to `int`.

    Examples:

        - `parse('abc OR x -> z')` returns `('z', 'OR', ('abc', 'x'))`

        - `parse('t RSHIFT 3 -> a')` returns `('a', 'RSHIFT', ('t', 3))`
            (the second element of the tuple, `3` is an `int`, ot a str `'3'`)

        - `parse('42 -> ever')` returns `('ever', 'SET', (42, ))`
            Note that 'SET' is not present (but only applied) in the input
            string, yet it is explicit in the parsed string. Also note that
            arguments is a tuple with a single element, `(42, )`.

        - `parse('NOT big -> small')` returns `('small', 'NOT', ('big')`
    """
    splited = s.split()
    if s.startswith("NOT"):
        return to_number(splited[-1]), "NOT", (to_number(splited[1]),)
    elif splited[1] == "->":
        return to_number(splited[-1]), "SET", (to_number(splited[0]),)
    else:
        return to_number(splited[-1]), splited[1], (to_number(splited[0]), to_number(splited[2]))


def read(filename):
    """Read a file with expressions (one in each line) into a list.

    Args:
        filename: the name of the file

    Returns:
        a list of expressions as tuples, such as returned by :obj:`parse`

    Example:

        If file input.txt looks like this::

            123 -> x
            456 -> y
            x AND y -> d
            x OR y -> e
            x LSHIFT 2 -> f
            y RSHIFT 2 -> g
            NOT x -> h
            NOT y -> i

        then `read('input.txt')` must return the following list::

            [('x', 'SET', (123,)),
             ('y', 'SET', (456,)),
             ('d', 'AND', ('x', 'y')),
             ('e', 'OR', ('x', 'y')),
             ('f', 'LSHIFT', ('x', 2)),
             ('g', 'RSHIFT', ('y', 2)),
             ('h', 'NOT', ('x',)),
             ('i', 'NOT', ('y',))]
    """
    return [parse(x) for x in (open(filename).readlines())]


# Ocena 7 / Grade 7

def inputs(exprs):
    """Return a set of names of all variables that appear as arguments

    Args:
        exprs (list): a list of expressions, like those returned be :obj:`read`

    Returns:
        set: a set of variable names

    Examples:

        Call ::

            outputs([('a', 'SET', ('b',)),
                     ('e', 'AND', (12, 'x')),
                     ('x', 'AND', ('z', 5))]`

        returns `{'b', 'x', 'z'}`. Note that 12 and 5 are absent from the list
        since these are not variables.
    """
    return {x for inputs_p, logic, output in exprs for x in output if not str(x).isdigit()}


def outputs(exprs):
    """Return a set of names of all variables that are computed by expressions

    Args:
        exprs (list): a list of expressions, like those returned be :obj:`read`

    Returns:
        set: a set of variable names

    Examples:

        Call ::

            outputs([('a', 'SET', ('b',)),
                     ('e', 'AND', (12, 'x')),
                     ('x', 'AND', ('z', 5))]`

        returns `{'a', 'e', 'x'}`
    """
    return {x for inputs_p, logic, output in exprs for x in inputs_p if not str(x).isdigit()}


def check_names(exprs):
    """Check whether all inputs are also computed by some expression

    Args:
        exprs (list): a list of expressions

    Returns:
        bool: `True` if all inputs also appear as outputs of some expression
    """
    return inputs(exprs) <= outputs(exprs)


def check_operators(exprs):
    """Check the validity of operator names

    Valid operator names are SET, NOT, AND, OR, LSHIFT and RSHIFT

    Args:
        exprs (list): a list of expressions

    Returns:
        bool: `True` if all operators are valid

    Example:

        The function returns `False` for a list like this::

            [('a', 'SET', ('b',)),
             ('e', 'LSHIFT', (12, 'x')),
             ('f', 'NOSUCHTHING', ('z', 5)),
             ('g', 'OR', (7, 5)),
             ('b', 'NOT', ('c',))]
    """
    return all([1 if operator in valid_operators else 0 for i, operator, o in exprs])


# Ocena 8

def get_value(name, variables):
    """Return the value corresponding to the name.

    Args:
        name (str or int): the name of a variable or an `int`
        variables (dict): a dictionary with variables names as keys and their
            values as values

    Returns:
        int: the value of the variable or the integer given as argument

    The function assumes that the name exists in the dictionary.

    Examples:

        - `get_value(42, {'a': 13, 'foo': -65)` returns `42`
        - `get_value('foo', {'a': 13, 'foo': -65)` returns `-65`
    """
    return name if str(name).isdigit() else variables[name]


def get_values(args, variables):
    """Return the tuple of values corresponding to the names in the tuple.


    Args:
        args: a tuple of `str` and/or `int`
        variables (dict): a dictionary with variables names as keys and their
            values as values

    Returns:
        tuple: values of variables as `int`

    The function is similar to :obj:`get_value` except that it takes a tuple
    and returns a tuple.

    Example:

        `get_values(('foo', 42), {'a': 13, 'foo': -65)` returns `(-65, 42)`

    """
    return tuple([val if str(val).isdigit() else variables[val] for val in args])


def compute_expr(op, args):
    """Compute an expression

    Args:
        op: operator, one of 'SET', 'NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT'
        args: arguments, given as a tuple with one or two `int`

    Returns:
        int: result of an expression

    The function assumes that the operator is valid and that the number of
    arguments matches the operator type.

    Operations are interpreted as bitwise, not logical operations.
    The function uses Python built-in operators `~` for NOT, `&` for AND,
    `|` for OR, `<<` for LSHIFT and `>>` for RSHIFT.

    Let `a` and `b` be the first and the second argument (if there are two).
    The function works as follows. If the operator is

    - "SET", result is `a`,
    - "NOT", result is  `~a` (note: tilde, not minus),
    - "AND" and "OR", results are `a  AND b` and `a OR b`, respectively,
    - "LSHIFT" and "RSHIFT", results are `a << b` and `a >> b`, respectively.

    Examples:

        - `compute_expr("SET", (12, ))` returns 12
        - `compute_expr("AND", (13, 69))` returns 5, computed as `13 & 69`
    """
    if op == "SET":
        return args[0]
    elif op == "NOT":
        return ~args[0]
    elif op == "AND":
        return args[0] & args[1]
    elif op == "OR":
        return args[0] | args[1]
    elif op == "LSHIFT":
        return args[0] << args[1]
    elif op == "RSHIFT":
        return args[0] >> args[1]


def compute_list(exprs):
    """Compute a list of expressions; return a dictionary with names and values

    Args:
        exprs (list): a list of expressions

    Returns:
        dict: dictionary with names of output variables and the corresponding
            values

    The function assumes (without checking) that expressions are valid and
    that they can be evaluated from top to bottom.

    Example:

        Call ::

            compute_list([('a', 'SET', (12,)),
                          ('b', 'NOT', ('a',)),
                          ('c', 'LSHIFT', ('a', 2)),
                          ('d', 'AND', ('b', 'c'))])

        returns `{'a': 12, 'b': -13, 'c': 48, 'd': 48}`, which corresponds to
        `{'a': 12, 'b': ~12, 'c': 12 << 2, 'd': ~12 & (12 << 2)}`.
    """
    s = {}
    for o, op, i in exprs:
        s[o] = compute_expr(op, get_values(i, s))
    return s


# Ocena 9

def dict_expr(exprs):
    """Construct a dictionary from a list of expressions

    Args:
        exprs (list): a list of expressions

    Returns:
        dict: dictionary with names of output variables as keys and tuples with
            operands and arguments as values

    Example:

        Call ::

            dict_expr([('a', 'SET', (12,)),
                       ('b', 'NOT', ('a',)),
                       ('c', 'LSHIFT', ('a', 2)),
                       ('d', 'AND', ('b', 'c'))])

        returns ::

            {'a': ('SET', (12,)),
             'b': ('NOT', ('a', )),
             'c': ('LSHIFT', ('a', 2)),
             'd': ('AND', ('b', 'c'))}
    """
    return {o: (op, i) for o, op, i in exprs}


def compute(var, exprs, variables):
    """Return the value of a variable given a list of expressions and values

    This function is similar to :obj:`compute_list` except that it evaluates
    the expressions in a different order if needed. For instance, it computes

        [('b', 'SET', ('a',)),
         ('a', 'SET', (42, ))]

    by first computing `a` and then `b`.

    The function assumes that the list of expressions is valid and that
    each variable appears as output only once.

    The function may modify the dictionary `variables` by adding the
    intermediate results, that is, the values of variables that are computed
    in while computing the value of the target variable `var`.

    Args:
        var (str): the name of the variable to compute
        exprs (list): a list of expressions
        variables (dict): known variable values

    Returns:
        int: the value of variable `var`

    Examples:

        Call `compute('b', [('b', 'SET', ('a',)), ('a', 'SET', (42, ))], {})`
        returns `42`.

        Call `compute('b', [('b', 'SET', ('a',))], {'a': 42})` also returns
        `42`.
    """
    op, arg = exprs[var]
    for e in arg:
        if not str(e).isdigit() and e not in variables:
                variables[e] = compute(e, exprs, variables)
    return compute_expr(op, get_values(arg, variables))


def compute_file(var, filename):
    """Return the value of a variable for the expressions in the given file.

    The function is similar to compute except that it reads expressions from
    the file and then calls `compute`.

    Args:
        var (str): the name of the variable to compute
        filename (str): file name

    Returns:
        int: the value of `var`
    """
    return compute(var, dict_expr(read(filename)), {})


# Ocena 10

def computable(exprs):
    """Check whether the list of expressions is computable.

    The list is not computable is some variables appear as outputs without
    appearing as inputs or if there are cycles, like in the following case::

        [('a', 'SET', ('b',)),
         ('b', 'SET', ('c',)),
         ('c', 'SET', ('a',))

    Note that cycles can also be more complicated, like in this case ::

        [('a', 'AND', ('b', 'd')),
         ('b', 'AND', ('c', 'd')),
        ('c', 'LSHIFT', ('f', 2)),
        ('d', 'OR', ('c', 'f')),
        ('e', 'NOT', ('d',)),
        ('f', 'SET', ('g',)),
        ('g', 'SET', ('a',))]

    where *g* needs *a*, *a* needs *b* and *d*, *b* needs *c* and *d*,
    *c* needs *f* and *f* needs *g*, which completes the cycle.

    Args:
        exprs (list): a list of expressions

    Returns:
        bool: `True` if expressions can be evaluated, `False` otherwise
"""
    if not check_names(exprs):
        return False
    variables = {}
    dexprs = dict_expr(exprs)
    try:
        for var, op, args in exprs:
            compute(var, dexprs, variables)
    except:
        return False
    return True


import unittest
from itertools import permutations


class Test06(unittest.TestCase):
    def test_to_number(self):
        self.assertEqual(to_number("42"), 42)
        self.assertEqual(to_number("156"), 156)
        self.assertEqual(to_number("1"), 1)
        self.assertEqual(to_number("123456789"), 123456789)

        self.assertEqual(to_number("a"), "a")
        self.assertEqual(to_number("abc"), "abc")
        self.assertEqual(to_number("I know places we can hide"), "I know places we can hide")

    def test_parse_set(self):
        self.assertIsInstance(parse("123 -> ax"), tuple, "`parse` must return a tuple")
        t = parse("123 -> ax")[-1]
        self.assertIsInstance(t, tuple,
                              "the last element of result of `parse` must be a tuple, not {}".format(type(t).__name__))

        self.assertEqual(parse("123 -> ax"), ("ax", "SET", (123,)))
        self.assertEqual(parse("9 -> blabla"), ("blabla", "SET", (9,)))
        self.assertEqual(parse("42 -> b"), ("b", "SET", (42,)))
        self.assertEqual(parse("abc -> b"), ("b", "SET", ("abc",)))

    def test_parse_not(self):
        self.assertIsInstance(parse("NOT 123 -> ax"), tuple, "`parse` must return a tuple")
        t = parse("NOT 123 -> ax")[-1]
        self.assertIsInstance(t, tuple,
                              "the last element of result of `parse` must be a tuple, not {}".format(type(t).__name__))

        self.assertEqual(parse("NOT 123 -> ax"), ("ax", "NOT", (123,)))
        self.assertEqual(parse("NOT 9 -> blabla"), ("blabla", "NOT", (9,)))
        self.assertEqual(parse("NOT 42 -> b"), ("b", "NOT", (42,)))
        self.assertEqual(parse("NOT abc -> b"), ("b", "NOT", ("abc",)))

    def test_parse_binary(self):
        self.assertIsInstance(parse("x AND yyy -> dd"), tuple, "`parse` must return a tuple")
        t = parse("x AND yyy -> dd")[-1]
        self.assertIsInstance(t, tuple,
                              "the last element of result of `parse` must be a tuple, not {}".format(type(t).__name__))

        self.assertEqual(parse("x AND yyyyyy -> dd"), ("dd", "AND", ("x", "yyyyyy")))
        self.assertEqual(parse("abc OR x -> z"), ("z", "OR", ("abc", "x")))
        self.assertEqual(parse("abc OR 15 -> z"), ("z", "OR", ("abc", 15)))
        self.assertEqual(parse("42 OR 15 -> z"), ("z", "OR", (42, 15)))
        self.assertEqual(parse("42 OR e -> z"), ("z", "OR", (42, "e")))
        self.assertEqual(parse("abc LSHIFT x -> z"), ("z", "LSHIFT", ("abc", "x")))
        self.assertEqual(parse("abc RSHIFT x -> z"), ("z", "RSHIFT", ("abc", "x")))

    def test_read(self):
        self.assertEqual(read("input1.txt"),
                         [('x', 'SET', (123,)), ('y', 'SET', (456,)), ('d', 'AND', ('x', 'y')), ('e', 'OR', ('x', 'y')),
                          ('f', 'LSHIFT', ('x', 2)), ('g', 'RSHIFT', ('y', 2)), ('h', 'NOT', ('x',)),
                          ('i', 'NOT', ('y',))])


class Test07(unittest.TestCase):
    def test_outputs(self):
        p = read("input1.txt")
        self.assertSetEqual(outputs(p), set('xydefghi'))

        self.assertSetEqual(outputs(
                [('a', 'SET', ('b',)), ('e', 'AND', (12, 'x')), ('f', 'AND', ('z', 5)), ('g', 'OR', (7, 5)),
                 ('b', 'NOT', ('c',))]), set('aefbg'))

        self.assertSetEqual(outputs([('a', 'SET', ('b',))]), {'a'})
        self.assertSetEqual(outputs([]), set())

    def test_inputs(self):
        p = read("input1.txt")
        self.assertSetEqual(inputs(p), {'x', 'y'})

        self.assertSetEqual(inputs(
                [('a', 'SET', ('b',)), ('e', 'AND', (12, 'x')), ('f', 'AND', ('z', 5)), ('g', 'OR', (7, 5)),
                 ('b', 'NOT', ('c',))]), set('bxcz'))

        self.assertSetEqual(inputs([('a', 'SET', ('b',))]), {'b'})
        self.assertSetEqual(inputs([('a', 'AND', ('b', 'c'))]), {'b', 'c'})
        self.assertSetEqual(inputs([]), set())
        self.assertSetEqual(inputs([('a', 'SET', (12,)), ('b', 'AND', (12, 15))]), set())

    def test_check_names(self):
        p = read("input1.txt")
        self.assertTrue(check_names(p))
        self.assertTrue(check_names([]))
        self.assertTrue(check_names([('a', 'SET', (12,)), ('b', 'AND', (12, 15))]))

        self.assertFalse(check_names([('a', 'SET', ('b',))]))
        self.assertFalse(check_names([('a', 'AND', ('b', 'c'))]))
        self.assertFalse(check_names([('a', 'AND', (5, 'c'))]))
        self.assertFalse(check_names([('a', 'AND', ('b', 12))]))
        self.assertFalse(check_names(
                [('a', 'SET', ('b',)), ('e', 'AND', (12, 'x')), ('f', 'AND', ('z', 5)), ('g', 'OR', (7, 5)),
                 ('b', 'NOT', ('c',))]))

    def test_check_operators(self):
        self.assertTrue(check_operators([]))
        self.assertTrue(check_operators([('a', 'SET', (12,))]))
        self.assertTrue(check_operators([('a', 'SET', (12,)), ('b', 'AND', (12, 15))]))
        self.assertTrue(check_operators(
                [('a', 'SET', ('b',)), ('e', 'LSHIFT', (12, 'x')), ('f', 'RSHIFT', ('z', 5)), ('g', 'OR', (7, 5)),
                 ('b', 'NOT', ('c',))]))

        self.assertFalse(check_operators(
                [('a', 'WRONG', ('b',)), ('e', 'LSHIFT', (12, 'x')), ('f', 'RSHIFT', ('z', 5)), ('g', 'OR', (7, 5)),
                 ('b', 'NOT', ('c',))]))

        self.assertFalse(check_operators(
                [('a', 'SET', ('b',)), ('e', 'LSHIFT', (12, 'x')), ('f', 'NOSUCHTHING', ('z', 5)), ('g', 'OR', (7, 5)),
                 ('b', 'NOT', ('c',))]))

        self.assertFalse(check_operators(
                [('a', 'SET', ('b',)), ('e', 'LSHIFT', (12, 'x')), ('f', 'RSHIFT', ('z', 5)), ('g', 'OR', (7, 5)),
                 ('b', 'FAIL', ('c',))]))


class Test08(unittest.TestCase):
    def test_compute_expr(self):
        self.assertEqual(compute_expr("SET", (42,)), 42)
        self.assertEqual(compute_expr("SET", (123,)), 123)

        self.assertEqual(compute_expr("NOT", (42,)), ~42)
        self.assertEqual(compute_expr("NOT", (0,)), ~0)

        self.assertEqual(compute_expr("AND", (12, 24)), 12 & 24)
        self.assertEqual(compute_expr("AND", (1234, 45678)), 1234 & 45678)

        self.assertEqual(compute_expr("OR", (12, 24)), 12 | 24)
        self.assertEqual(compute_expr("OR", (1234, 45678)), 1234 | 45678)

        self.assertEqual(compute_expr("LSHIFT", (123, 1)), 123 << 1)
        self.assertEqual(compute_expr("LSHIFT", (123, 3)), 123 << 3)

        self.assertEqual(compute_expr("RSHIFT", (123, 1)), 123 >> 1)
        self.assertEqual(compute_expr("RSHIFT", (123, 3)), 123 >> 3)

    def test_get_value(self):
        t = {'a': 13, 'bcd': 42, 'agr': 66}
        self.assertEqual(get_value(42, t), 42)
        self.assertEqual(get_value(15, t), 15)
        self.assertEqual(get_value('bcd', t), 42)
        self.assertEqual(get_value('agr', t), 66)
        self.assertEqual(get_value(42, {}), 42)
        self.assertEqual(get_value('x', {'x': 12}), 12)

        self.assertRaises(KeyError, get_value, 'bcd', {})
        self.assertRaises(KeyError, get_value, 'bcd', {'x': 12})

    def test_get_values(self):
        t = {'a': 13, 'bcd': 42, 'agr': 66}
        self.assertEqual(get_values((42, 15), t), (42, 15))
        self.assertEqual(get_values((42, 15, 1, 8), t), (42, 15, 1, 8))
        self.assertEqual(get_values((15,), t), (15,))

        self.assertEqual(get_values(('a', 15), t), (13, 15))
        self.assertEqual(get_values((7, 'bcd'), t), (7, 42))
        self.assertEqual(get_values(('bcd', 'agr'), t), (42, 66))
        self.assertEqual(get_values(('bcd', 13, 'agr'), t), (42, 13, 66))

        t = {'a': 13, 'x': 42}
        self.assertEqual(get_values(('a', 15, 'x'), t), (13, 15, 42))

        self.assertRaises(KeyError, get_values, (7, 'bcd'), t)

    def test_compute_list(self):
        self.assertEqual(compute_list([('a', 'SET', (12,))]), {'a': 12})
        self.assertEqual(compute_list([('a', 'SET', (12,)), ('b', 'SET', (42,))]), {'a': 12, 'b': 42})

        self.assertEqual(compute_list([('a', 'SET', (12,)), ('b', 'SET', ('a',))]), {'a': 12, 'b': 12})

        self.assertEqual(compute_list([('a', 'SET', (12,)), ('b', 'NOT', ('a',))]), {'a': 12, 'b': ~12})

        self.assertEqual(compute_list(
                [('a', 'SET', (12,)), ('b', 'NOT', ('a',)), ('c', 'LSHIFT', ('a', 2)), ('d', 'AND', ('b', 'c'))]),
                {'a': 12, 'b': ~12, 'c': 12 << 2, 'd': ~12 & (12 << 2)})

        t = read("input1.txt")
        self.assertEqual(compute_list(t),
                         {'d': 72, 'x': 123, 'h': -124, 'y': 456, 'e': 507, 'f': 492, 'i': -457, 'g': 114})


class Test09(unittest.TestCase):
    def test_dict_expr(self):
        self.assertEqual(dict_expr([('a', 'SET', (12,))]), {'a': ('SET', (12,))})
        self.assertEqual(dict_expr([('a', 'SET', (12,)), ('b', 'SET', (42,))]),
                         {'a': ('SET', (12,)), 'b': ('SET', (42,))})

        self.assertEqual(dict_expr([('a', 'SET', (12,)), ('b', 'SET', ('a',))]),
                         {'a': ('SET', (12,)), 'b': ('SET', ('a',))})

        self.assertEqual(dict_expr(
                [('a', 'SET', (12,)), ('b', 'NOT', ('a',)), ('c', 'LSHIFT', ('a', 2)), ('d', 'AND', ('b', 'c'))]),
                {'a': ('SET', (12,)), 'b': ('NOT', ('a',)), 'c': ('LSHIFT', ('a', 2)), 'd': ('AND', ('b', 'c'))})

    def test_compute(self):
        t = read('input1.txt')
        izrazi = dict_expr(t)
        self.assertEqual(compute('i', izrazi, {}), -457)

        t = read('input2.txt')
        izrazi = dict_expr(t)
        self.assertEqual(compute('a', izrazi, {}), 46065)

    def test_compute_file(self):
        self.assertEqual(compute_file('i', 'input1.txt'), -457)
        self.assertEqual(compute_file('a', 'input2.txt'), 46065)


class Test10(unittest.TestCase):
    def test_computable(self):
        self.assertTrue(computable([('a', 'SET', (12,))]))
        self.assertTrue(computable([]))
        self.assertTrue(computable([('a', 'SET', (12,)), ('b', 'SET', (42,))]))
        self.assertTrue(computable([('a', 'SET', (12,)), ('b', 'SET', ('a',))]))
        self.assertTrue(computable([('a', 'SET', ('b',)), ('b', 'SET', (12,))]))
        for t in permutations(
                [('a', 'SET', (12,)), ('b', 'NOT', ('a',)), ('c', 'LSHIFT', ('a', 2)), ('d', 'AND', ('b', 'c'))]):
            u = t[:]
            self.assertTrue(computable(t))
            self.assertEqual(u, t)

        for t in permutations(
                [('a', 'AND', ('b', 'd')), ('b', 'AND', ('c', 'd')), ('c', 'LSHIFT', ('f', 2)), ('d', 'OR', ('c', 'f')),
                 ('e', 'NOT', ('d',)), ('f', 'SET', ('g',)), ('g', 'SET', (42,))]):
            u = t[:]
            self.assertTrue(computable(t))
            self.assertEqual(u, t)

        self.assertTrue(computable(read("input1.txt")))
        self.assertTrue(computable(read("input2.txt")))

    def test_missing_variables(self):
        self.assertFalse(computable([('a', 'AND', ('b', 12))]))
        self.assertFalse(computable([('a', 'AND', ('12', 'b'))]))
        self.assertFalse(computable([('a', 'AND', ('c', 'b'))]))

        self.assertFalse(computable(
                [('a', 'SET', (12,)), ('b', 'AND', ('a', 7)), ('c', 'NOT', ('a',)), ('d', 'AND', ('5', 'doesnotexist')),
                 ('e', 'AND', (7, 'b')), ]))

    def test_cycles(self):
        self.assertFalse(computable([('a', 'SET', ('b',)), ('b', 'SET', ('a',))]))
        self.assertFalse(computable([('a', 'SET', ('b',)), ('b', 'AND', ('a', 12))]))
        for t in permutations([('a', 'SET', ('b',)), ('b', 'SET', ('c',)), ('c', 'SET', ('d',)), ('d', 'SET', ('e',)),
                               ('e', 'SET', ('f',)), ('f', 'SET', ('g',)), ('g', 'SET', ('a',))]):
            u = t[:]
            self.assertFalse(computable(t))
            self.assertEqual(u, t)

        for t in permutations(
                [('a', 'AND', ('b', 'd')), ('b', 'AND', ('c', 'd')), ('c', 'LSHIFT', ('f', 2)), ('d', 'OR', ('c', 'f')),
                 ('e', 'NOT', ('d',)), ('f', 'SET', ('g',)), ('g', 'SET', ('a',))]):
            u = t[:]
            self.assertFalse(computable(t))
            self.assertEqual(u, t)

        for t in permutations(
                [('a', 'AND', ('b', 'd')), ('b', 'AND', ('c', 'd')), ('c', 'LSHIFT', ('e', 2)), ('d', 'OR', ('c', 'f')),
                 ('e', 'NOT', ('d',)), ('f', 'SET', ('g',)), ('g', 'SET', (42,))]):
            u = t[:]
            self.assertFalse(computable(t))
            self.assertEqual(u, t)


if __name__ == "__main__":
    unittest.main()
