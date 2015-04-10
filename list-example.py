nums = [1, 3, 2, 15, 10]

print "len:", len(nums)
print "sum:", sum(nums)
print "min:", min(nums)
print "max:", max(nums)

for num in nums:
    print num,
print 

print "range:", range(len(nums))

nums.sort()
print nums

for x in range(len(nums)):
    print "index:", x, "; num:", nums[x]

print dir(nums)

print nums[-1]
