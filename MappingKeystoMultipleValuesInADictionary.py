# You wanto to make a dictionary that maps keys to more than one value (multidict)

from collections import defaultdict

e = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

d = defaultdict(list)

for key, value in pairs:
    d[key].append(value)