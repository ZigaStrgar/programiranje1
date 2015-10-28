filmi = ['Poletje v skoljki 2', 'Ne cakaj na maj', 'Pod njenim oknom', 'Kekec', 'Poletje v skoljki', 'To so gadi']
ocene = [6.1, 7.3, 7.1, 8.1, 7.2, 7.7]

joined = zip(filmi, ocene)

for movie_title, movie_rating in joined:
    counter = 0
    for char in list(movie_title):
        if char == " ":
            counter += 1
    if counter == 2:
        print(movie_title, " (", movie_rating, ")", sep="")
