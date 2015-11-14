import collections
import unittest


def family_tree(family):
    kids = collections.defaultdict(list)
    for father, kid in family:
        kids[father].append(kid)
    return kids


def children(tree, name):
    return tree.get(name, [])


def grandchildren(tree, name):
    grandchild = []
    for name in tree.get(name, []):
        for name2 in tree.get(name, []):
            grandchild.append(name2)
    return grandchild


def successors(tree, name):
    successors_list = []
    goto = [name]
    while len(goto) > 0:
        new_name = goto.pop()
        goto.extend(children(tree, new_name))
        successors_list.extend(children(tree, new_name))
    return successors_list


def freq(xs):
    return collections.Counter(xs)
    """ctr = collections.defaultdict(int)
    for char in xs:
        ctr[char] += 1
    return ctr"""


def naj_freq(ctr):
    return ctr.most_common(1)[0][0]
    """naj = 0
    for key, value in ctr.items():
        if value > naj:
            naj = value
            naj_key = key
    return naj_key"""


def najpogostejse(s):
    return naj_freq(freq(s.split())), naj_freq(freq(s))


def najpogostejse2(s):
    pogosta_crka = collections.defaultdict(int)
    for char in s:
        pogosta_crka[char] += 1
    pogosta_beseda = collections.defaultdict(int)
    for word in s.split(" "):
        pogosta_beseda[word] += 1
    najcrka = None
    najcrka_z = None
    for key, val in pogosta_crka.items():
        if not najcrka or val > najcrka:
            najcrka = val
            najcrka_z = key
    najbeseda = None
    najbeseda_z = None
    for key, val in pogosta_beseda.items():
        if not najbeseda or val > najbeseda:
            najbeseda = val
            najbeseda_z = key

    return najbeseda_z, najcrka_z


def wordss(s):
    words = set()
    for word in s.split():
        words.add(word)
    return list(words)


def nasledniki(s):
    nexts = collections.defaultdict(list)
    for word in wordss(s):
        nextt = 0
        for word2 in s.split():
            if nextt == 1:
                nexts[word].append(word2)
            if word == word2:
                nextt = 1
                continue
            nextt = 0
    return nexts


class TestNaloge5(unittest.TestCase):
    def setUp(self):
        self.tree = {
            'alice': ['mary', 'tom', 'judy'],
            'bob': ['mary', 'tom', 'judy'],
            'ken': ['suzan'],
            'renee': ['rob', 'bob'],
            'rob': ['jim'],
            'sid': ['rob', 'bob'],
            'tom': ['ken']}

    def assertDictCounterEqual(self, first, second, msg=None):
        def dict_counter(d):
            d_copy = dict(d)
            for k, v in d_copy.items():
                d_copy[k] = collections.Counter(v)
            return d_copy

        self.assertDictEqual(dict_counter(first), dict_counter(second), msg)

    def test_family_tree(self):
        family = [
            ('bob', 'mary'),
            ('bob', 'tom'),
            ('bob', 'judy'),
            ('alice', 'mary'),
            ('alice', 'tom'),
            ('alice', 'judy'),
            ('renee', 'rob'),
            ('renee', 'bob'),
            ('sid', 'rob'),
            ('sid', 'bob'),
            ('tom', 'ken'),
            ('ken', 'suzan'),
            ('rob', 'jim')]
        self.assertDictCounterEqual(family_tree(family), self.tree)

    def test_children(self):
        self.assertCountEqual(children(self.tree, 'alice'), ['mary', 'tom', 'judy'])
        self.assertCountEqual(children(self.tree, 'mary'), [])
        self.assertCountEqual(children(self.tree, 'renee'), ['bob', 'rob'])
        self.assertCountEqual(children(self.tree, 'rob'), ['jim'])
        self.assertCountEqual(children(self.tree, 'suzan'), [])

    def test_grandchildren(self):
        self.assertCountEqual(grandchildren(self.tree, 'alice'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'bob'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'ken'), [])
        self.assertCountEqual(grandchildren(self.tree, 'mary'), [])
        self.assertCountEqual(grandchildren(self.tree, 'renee'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'sid'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'tom'), ['suzan'])

    def test_successors(self):
        self.assertCountEqual(successors(self.tree, 'tom'), ['ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'sid'),
                              ['rob', 'bob', 'jim', 'mary', 'tom', 'judy', 'ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'suzan'), [])
        self.assertCountEqual(successors(self.tree, 'ken'), ['suzan'])
        self.assertCountEqual(successors(self.tree, 'rob'), ['jim'])

    def test_najpogostejse(self):
        self.assertEqual(najpogostejse('a'), ('a', 'a'))
        self.assertEqual(najpogostejse('aa bb aa'), ('aa', 'a'))
        self.assertEqual(najpogostejse('in to in ono in to smo mi'), ('in', ' '))
        self.assertEqual(najpogostejse('abc abc abc abacbca'), ('abc', 'a'))
        self.assertEqual(najpogostejse('abc abc abc abacbcb'), ('abc', 'b'))
        self.assertEqual(najpogostejse('abc abc abc abacbcc'), ('abc', 'c'))

    def test_najpogostejse_urejene(self):
        self.assertEqual(najpogostejse_urejene('a'), (['a'], ['a']))
        self.assertEqual(najpogostejse_urejene('aa bb aa'), (['aa', 'bb'], ['a', ' ', 'b']))
        self.assertEqual(najpogostejse_urejene('in to in ono in to smo mi'),
                         (['in', 'to', 'mi', 'ono', 'smo'], [' ', 'o', 'i', 'n', 'm', 't', 's']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbca'),
                         (['abc', 'abacbca'], ['a', 'b', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcb'),
                         (['abc', 'abacbcb'], ['b', 'a', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcc'),
                         (['abc', 'abacbcc'], ['c', 'a', 'b', ' ']))

    def test_sifra(self):
        self.assertEqual(sifra('\x19\x14\x1c]\x19\x0f\x14\t\x13\x18\t]\x12\x0e[\n\x1a\t\x18\x15\x12\x13\x1c'),
                         'big brother is watching')
        self.assertEqual(sifra('\xe1d\xe0q\xe5r\xf7b\xe0i'), 'strawberry')

    def test_nasledniki(self):
        self.assertDictCounterEqual(nasledniki('in in in in'), {'in': ['in', 'in', 'in']})
        self.assertDictCounterEqual(nasledniki('in to in ono in to smo mi'),
                                    {'smo': ['mi'], 'to': ['in', 'smo'], 'ono': ['in'], 'in': ['to', 'ono', 'to']})
        self.assertDictCounterEqual(nasledniki('danes je lep dan danes sije sonce'),
                                    {'lep': ['dan'], 'je': ['lep'], 'dan': ['danes'], 'danes': ['je', 'sije'],
                                     'sije': ['sonce']})

    def test_tekst(self):
        self.assertEqual(tekst({'in': ['in', 'in']}, 3), 'in in in')


if __name__ == '__main__':
    unittest.main(verbosity = 2)
