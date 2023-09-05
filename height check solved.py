
heights = [1,2,4,3,5,9,8]
d = heights
m = sorted(heights)

a = [x for x,y in zip(d, m) if x!= y]
print(a)