# Ypu want to create a dictionary, and you also want to control the order of item when iterating or serializing.

from collections import OrderedDict # preserve the insertion order
import json

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key]) #Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    
json.dumps(d)