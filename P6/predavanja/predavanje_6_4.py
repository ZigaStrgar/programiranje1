ime = "benjamin"
ime1 = "robi"
ime2 = "berta"
ime3 = "oto"

m_ime = set(ime)
m_ime1 = set(ime1)
m_ime2 = set(ime2)
m_ime3 = set(ime3)

print(m_ime & m_ime2)
print(len(set(ime) & set(ime2)))  # Presek
{1, 3, 5} | {5, 7}  # Unija
{1, 3, 5} - {7, 3}  # Odštevanje
{1, 3} < {1, 3, 5}  # Odštevanje
{1, 3} < {1, 3}  # Podmnožica - FALSE!!!
{1, 3} <= {1, 3}  # Podmnožica - TRUE!!!
{1, 3, 5} > {1, 3}  # Nadmnožica - TRUE!!!
