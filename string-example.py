# String example of python by Dong Zhou

first_name = "dong"
last_name = "zhou"
full_name  = first_name + " " +  last_name

print full_name[::-1]

print full_name[::2]

print "Hello World!"

print "first name: " + first_name

print "last name: " + last_name

print "full name: " + full_name

print "first element of first name: " + first_name[0]

print "second element of last name: " + last_name[1]

print "last element of first name: " + first_name[-1]

print "second last elment of last name: " + last_name[-2]

print "first three elment of full_name: " + full_name[:3]

print "second to sixth elements of full_name: " + full_name[1:6]

print "all the elements of full_name one by one: ",  # add ',' to not change row
for i in full_name:
    print i,
print

print "mutiply first name: " + first_name * 3

print "mutiply last name: " + 5 * last_name
