x = ("apple", "banana", "melon")

y = (1, 9, 3)

print x

print y

for item in x:
    print item

for item in y:
    print item

print dir(x)

(a, b) = (99, 98)

print a

print b

c = {"a": 10, "b":1, "c": 22}

type(c)

print c

# this is amazing thing, enjoy python
print sorted([(v, k) for k, v in c.items()])
