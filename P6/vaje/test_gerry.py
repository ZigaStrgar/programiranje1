import unittest


def str2ints(s):
    numbers = []
    for char in s.split():
        numbers.append(int(char))
    return numbers


def preberi():
    lines = open('gerry.in').readlines()
    for num, line in enumerate(lines):
        if line == "\n":
            count = num + 1
            case, w, h, d = lines[count].split()
            w, h, d = int(w), int(h), int(d)
            count += 1
            number = 0
            sections = []
            while number < h:
                if lines[count] == "\n":
                    break
                sections.append(str2ints(lines[count]))
                count += 1
                number += 1
    return w, h, d, sections


def simple_sol(w, h, d, f):
    rez = []
    nh = 0
    count = 0
    while nh < h:
        new_line = []
        nw = 0
        while nw < w:
            if count > d - 1:
                count = d - 1
            new_line.append(count)
            count += 1
            nw += 1
        rez.append(new_line)
        nw = 0
        nh += 1
    return rez


def sestej(sez):
    vsota = 0
    for num in sez:
        vsota += int(num)
    return vsota


def score(w, h, d, f, solution):
    vmes = []
    n = 0
    while n < d:
        vmes.append(0)
        n += 1
    new_list = []
    for num, line in enumerate(f):
        new_list.append(zip(line, solution[num]))
    for line in new_list:
        for ppl, dist in line:
            vmes[dist] += ppl
    return sorted(vmes)[-1] - sorted(vmes)[0]


def floodfill(w, h, d, f, sollutions, start_y, start_x):
    replace = sollutions[start_y][start_x]
    for nr, row in enumerate(sollutions):
        for n, e in enumerate(row):
            if e == replace:
                sollutions[nr][n] = -1
    print(sollutions)
    return sollutions


def num_components(w, h, d, f, sollutions):
    return d


class TestGerry(unittest.TestCase):
    def test_str2ints(self):
        self.assertEqual(str2ints(''), [])
        self.assertEqual(str2ints('1'), [1])
        self.assertEqual(str2ints('1 2'), [1, 2])
        self.assertEqual(str2ints('1 2 5 99 1234 -123'), [1, 2, 5, 99, 1234, -123])

    def test_preberi(self):
        self.assertEqual(preberi(), (4, 3, 3, [[3, 3, 2, 1], [2, 2, 7, 0], [3, 4, 1, 1]]))

    def test_simple_sol(self):
        x = (4, 3, 3, [[3, 3, 2, 1], [2, 2, 7, 0], [3, 4, 1, 1]])
        self.assertEqual(simple_sol(*x), [[0, 1, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]])
        x = (2, 2, 2, [[3, 3], [2, 2]])
        self.assertEqual(simple_sol(*x), [[0, 1], [1, 1]])

    def test_score(self):
        x = (4, 3, 3, [[3, 3, 2, 1], [2, 2, 7, 0], [3, 4, 1, 1]])
        self.assertEqual(score(*x, [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]]), 2)
        self.assertEqual(score(*x, [[0, 0, 0, 2], [1, 0, 2, 2], [1, 1, 2, 2]]), 1)
        self.assertEqual(score(*x, [[0, 1, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]), 20)
        self.assertEqual(score(*x, [[0, 0, 1, 2], [0, 0, 1, 2], [0, 0, 1, 2]]), 15)

    def test_floodfill(self):
        x = (4, 3, 3, [[3, 3, 2, 1], [2, 2, 7, 0], [3, 4, 1, 1]])
        self.assertEqual(floodfill(*x, [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], 0, 0),
                         [[-1, -1, -1, -1], [1, 1, 1, 1], [2, 2, 2, 2]])
        self.assertEqual(floodfill(*x, [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], 0, 2),
                         [[-1, -1, -1, -1], [1, 1, 1, 1], [2, 2, 2, 2]])
        self.assertEqual(floodfill(*x, [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], 1, 2),
                         [[0, 0, 0, 0], [-1, -1, -1, -1], [2, 2, 2, 2]])
        self.assertEqual(floodfill(*x, [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]], 0, 2),
                         [[-1, -1, -1, -1], [1, 1, 1, 1], [0, 0, 0, 0]])
        self.assertEqual(floodfill(*x, [[0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 0, 0),
                         [[-1, 1, -1, -1], [-1, 1, 1, -1], [-1, -1, -1, -1]])
        self.assertEqual(floodfill(*x, [[0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 0, 1),
                         [[0, -1, 0, 0], [0, -1, -1, 0], [0, 0, 0, 0]])
        self.assertEqual(floodfill(*x, [[0, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]], 0, 0),
                         [[-1, 1, 0, 0], [-1, 1, 1, 1], [-1, -1, -1, -1]])

    def test_num_components(self):
        x = (4, 3, 3, [[3, 3, 2, 1], [2, 2, 7, 0], [3, 4, 1, 1]])
        self.assertEqual(num_components(*x, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), 1)
        self.assertEqual(num_components(*x, [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]), 12)
        self.assertEqual(num_components(*x, [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]]), 3)
        self.assertEqual(num_components(*x, [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]]), 3)
        self.assertEqual(num_components(*x, [[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0]]), 3)
        self.assertEqual(num_components(*x, [[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0]]), 2)
        self.assertEqual(num_components(*x, [[0, 1, 0, 2], [0, 1, 0, 2], [0, 1, 0, 2]]), 4)


if __name__ == '__main__':
    unittest.main(verbosity = 2, warnings = 'ignore')
