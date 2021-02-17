# You have an N-element tuple or sequence that you would like to unpack into a collection of N variables

p = (4, 5)
x,y = p

print("x = ", x)
print("y = ", y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

print("name = ", name)
print("shares = ", shares)
print("price = ", price)
print("data = ", date)
print("year = ", year)
print("mon = ", mon)
print("day = ", day)

# Unpacking works with any object that is iterable, like strings

s = 'Hello'

a, b, c, d, e = s

# It's possible to discard values by using underscore or by picking a throwaway variable name that has not been used.