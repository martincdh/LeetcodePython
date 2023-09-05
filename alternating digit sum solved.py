n =886996
n = str(n)
count = 0
for i in range(len(n)):
    if i%2 == 0:
        count+=int(n[i])
    else:
        count -= int(n[i])

print(count)