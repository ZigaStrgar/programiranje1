def tekac(startna, ime, leto, h, m, s):
    return "{0:>4}. {1:20} {2:0>2}:{3:0>2}:{4:0>2}".format(startna, ime, h, m, s)


def tekac_star(startna, ime, leto, h, m, s):
    leto = "("+str(leto)+")"
    return "{0:>4}. {1} {2:<14} {3:0>2}:{4:0>2}:{5:0>2}".format(startna, ime, leto, h, m, s)

import unittest
class TestTekaci(unittest.TestCase):
    def test_tekac(self):
        self.assertEqual(tekac(1, "ROMAN SONJA", 1979, 1, 15, 2),
                         "   1. ROMAN SONJA          01:15:02")
        self.assertEqual(tekac(1234, "ROMAN SONJA", 1979, 0, 1, 23),
                         "1234. ROMAN SONJA          00:01:23")

    def test_tekac_star(self):
        self.assertEqual(tekac_star(1, "ROMAN SONJA", 1979, 1, 15, 2),
                         "   1. ROMAN SONJA (1979)         01:15:02")
        self.assertEqual(tekac_star(1234, "ROMAN SONJA", 1979, 0, 1, 23),
                         "1234. ROMAN SONJA (1979)         00:01:23")

if __name__ == "__main__":
    unittest.main()
