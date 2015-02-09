# tuple, list, dictionary

tuple_one = (1, "two", 3)
print tuple_one,
print type(tuple_one)
print "two" in tuple_one

tuple_two = (tuple_one, "four")
print tuple_two

tuple_three = tuple_one + tuple_two
print tuple_three
print tuple_three[4]
print tuple_three[0:4]

for element in tuple_three:
    print element

tuple_four = ("five")
print tuple_four
print type(tuple_four)

#singletons
tuple_five = ("five",)
print tuple_five
print type(tuple_five)

list_one = [1, "two", 3]
print list_one,
print type(list_one)
list_one[0] = "one"
print list_one,
print type(list_one)

list_two = [list_one, "a", "b", "c"]
print list_two
print "a" in list_two
list_two.remove("a")
print "a" in list_two

list_three = list_one + list_two
print list_three

for element in list_three:
    print element, 
    print type(element)

list_three.append("append")
print list_three

#clone
list_four = list_three[:]
list_three.remove("b")

print list_three
print list_four

dict_one = {1: "one", "two": 2, 3 : "Mar"}
print dict_one
print dict_one[1],
print dict_one["two"]

dict_one[4] = "Apr"
dict_one[6] = "Jun"
print dict_one

del dict_one[6]
print dict_one

print dict_one.pop(3)
print dict_one
