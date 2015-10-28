xs = ['foo', 'bar', 'baz', 'Waldo', 'foobar']
contains = False

for string in xs:
    if string == "Waldo":
        contains = True
        break
print(contains)
