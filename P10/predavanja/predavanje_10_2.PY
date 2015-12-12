def vsota(s):
    v = 0
    for e in s:
        v += e
    return v


def vsota(s):
    if not s:
        return 0
    return s[0] + vsota(s[1:])


def ni_lihih(s):
    if not s:
        return True
    if s[0] % 2 == 1:
        return False
    return ni_lihih(s[1:])


def ni_lihih(s):
    return not s or s[0] % 2 == 0 and ni_lihih(s[1:])


def palindrom(s):
    return len(s) <= 1 or s[0] == s[-1] and palindrom(s[1:-1])


print(ni_lihih([7, 4, 1, 3]))
