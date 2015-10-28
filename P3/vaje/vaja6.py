filmi = [
    ('Poletje v skoljki 2', 6.1),
    ('Ne cakaj na maj', 7.3),
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1),
    ('Poletje v skoljki', 7.2),
    ('To so gadi', 7.7),
]

print("Vsi filmi z vsaj 7.0 oceno")
for movie_title, movie_rating in filmi:
    if movie_rating > 7:
        print(movie_title)

print("\n\n")

print("Film z najvišjo oceno")
maximum = 0
max_title = ""
for movie_title, movie_rating in filmi:
    if movie_rating > maximum:
        maximum = movie_rating
        max_title = movie_title
print(max_title)

print("\n\n")

print("Prvi film z vsaj 7.0")
for movie_title, movie_rating in filmi:
    if movie_rating > 7:
        print(movie_title)
        break

print("\n\n")

print("Povprečna ocena filmov")
vsota = 0
for movie_title, movie_rating in filmi:
    vsota += movie_rating
print(vsota / len(filmi))

print("\n\n")

print("Filmi z drugim delom")
for movie_title, movie_rating in filmi:
    for movie_title2, movie_rating2 in filmi:
        if (movie_title + " 2") == movie_title2:
            print(movie_title)
