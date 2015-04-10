dictionary = {"apple": 1, "banana": 10, "melon": 4}

print dictionary

print dictionary.get("car")

print dictionary.get("car", 0)

dictionary["car"] = 2

print dictionary

for item in dictionary:
    print item

# Which means by default, dict in python execyte its keys
if "melon" in dictionary:
    print "yes"
else:
    print "nope"

print dictionary.keys()

print dictionary.values()

print dictionary.items()

print dictionary

# This is amazing method, I become really like python
for k,v in dictionary.items():
    print k, v

print dir(dictionary)
