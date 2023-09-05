nums = [-3,-2,-1,0,0,1,2]
count = 0
d =0
for i in nums:
    if i < 0:
        count+=1
    elif i > 0:
        d+=1

if count > d:
    print(count)
else:
    print(d)