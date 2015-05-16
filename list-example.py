nums = [1, 3, 2, 15, 10]

print "len:", len(nums)
print "sum:", sum(nums)
print "min:", min(nums)
print "max:", max(nums)

for num in nums:
    print num,
print 

print "range:", range(len(nums))

# nums.sort()
print nums

for x in range(len(nums)):
    print "index:", x, "; num:", nums[x]

print dir(nums)

print nums[-1]

# this is amazing, the position of 10 in the list
print nums.index(10)

nums.append(4)

print nums

print nums.pop(1)

print nums

print nums.pop()

print nums

print nums.count(2)
nums.append(2)
print nums.count(2)

# I really like python now! list method:
# 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# get index and value of list in same time
choices = ['pizza', 'pasta', 'salad', 'nachos']
print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item

