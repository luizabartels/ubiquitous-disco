# You need to unpack N elements from an iterable, but the iteraple may be longer than N elements, causing s "too many 
# values to unpack" exception

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

# When we use a * with a variable, we make a list of values

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)
    
def do_bar(s):
    print('bar', s)

# Nesse laço abaixo, sempre depois de uma tag vem uma sequência de valores. Sabendo disso, armazena-se todos os valores 
# após a tag na variável com a sintaxe * e e então chamaria a função para fazer o unpacking

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        
# Another example
        
items = [1, 10, 7, 4, 5, 9]
head, *tail = items

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

sum(items)