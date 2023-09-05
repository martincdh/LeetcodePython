x = 234
x = str(x)
pro =1
s = 0


for i in range(len(x)):
    s += int(x[i])
    pro *= int(x[i])

final = pro - s
print(final)


abc = [1,2,1]
x = abc.count(1)
print(x)


i = "10"
m = sum([int(x) for x in str(i)])
print(m)