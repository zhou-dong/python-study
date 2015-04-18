# Set in Python: 
#   1. no duplicate; 
#   2. no order

test = set([1,2,3])

print test

test = set([1,2,1,2,3,1,3,3])

print test

test.add(1)
test.add(4)
test.add(5)
test.add("cool")

print test

test.remove(5)

print test

for x in test:
    print x
