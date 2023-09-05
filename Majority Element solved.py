nums = [3,3,4]
x = list(set(nums))
max_s = 1
for i in x:
    if nums.count(i) > max_s:
        max_s = nums.count(i)
        y = i

print(y)
x = nums.index(3)
print(x)


l1 = [1,2,3]
l2 = [1,1,2,3]
l3 = l2+l1
print(l3)