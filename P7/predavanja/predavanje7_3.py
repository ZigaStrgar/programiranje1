import os

file = open("planeti.txt")

for row in file:
    print(row.strip())

file = open("planeti.txt")
print(file.read())
