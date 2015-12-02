from math import sqrt

morse = {'A': '.-',
         'B': '-...',
         'C': '-.-.',
         'D': '-..',
         'E': '.',
         'F': '..-.',
         'G': '--.',
         'H': '....',
         'I': '..',
         'J': '.---',
         'K': '-.-',
         'L': '.-..',
         'M': '--',
         'N': '-.',
         'O': '---',
         'P': '.--.',
         'Q': '--.-',
         'R': '.-.',
         'S': '...',
         'T': '-',
         'U': '..-',
         'V': '...-',
         'W': '.--',
         'X': '-..-',
         'Y': '-.--',
         'Z': '--..',
         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.',
         '0': '-----',
         }


def vsota_kvadratov():
    return sum([x ** 2 for x in range(1, 101)])


def palindomska_vsota():
    return sum(x ** 2 for x in range(1, 1000) if str(x) == str(x)[::-1])


def zamenjava_crk(string, position):
    return "".join([string[int(i)] for i in position])


def mean(xs):
    return sum(xs) / len(xs)


def std(xs):
    return sqrt(sum([(x - mean(xs)) ** 2 for x in xs]) / len(xs))


def text2morse(string, morsecode):
    return " ".join([morsecode[char] if char != " " else "" for char in string])


def morse2text(string, morsecode):
    morsecode = dict(zip(morsecode.values(), morsecode.keys()))
    return "".join([morsecode[char] if char != "" else " " for char in string.split(" ")])


def valid(number):
    return (sum([(int(num) if num != "X" else 10) * (i + 1) for i, num in enumerate(number)])) % 11 == 0 and len(number) == 10


print(vsota_kvadratov())
print(palindomska_vsota())
print(zamenjava_crk("komar", "23401"))
print(mean([183, 168, 175, 176, 192, 180]))
print(std([183, 168, 175, 176, 192, 180]))
print(text2morse("TE A", morse))
print(morse2text('.... . .-.. .-.. ---  .-- --- .-. .-.. -..', morse))
print(valid('0306406152'))
print(valid('0553382578'))
print(valid('0553293370'))
print(valid('03064061522'))
print(valid('1553382578'))
print(valid('91211562811'))
print(valid('912115628X'))
