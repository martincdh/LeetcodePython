import math
nums = [43,9,75,76,25,96,46,85,19,29,88,2,5,24,60,26,76,24,96,82,97,97,72,35,21,77,82,30,94,55,76,94,51]
d = 0
count =0
for i in nums:
    if i%3 == 0 and i%2 ==0:
        d+=i
        count+=1
if count >=1:
    x = d/count
    print(x)
    print(d)
    print(count)
else:
    print(0)
