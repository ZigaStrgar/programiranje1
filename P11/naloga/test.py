def compute(var, exprs, variables):
    if var in variables.keys():
        return variables[var]
    op, args = exprs[var]
    for arg in args:
        if var not in variables.keys():
            variables = compute(arg, exprs, variables)
    return variables[var]

compute('b', {'b': ('SET', ('a',)), 'a': ('SET', (42, ))}, {})
