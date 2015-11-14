import collections

s = collections.defaultdict()

s = collections.defaultdict(int)

s["stol"]  # Izpiše 0
s["miza"] += 100  # Tudi če ne obstaja prišteje 0 + 100

