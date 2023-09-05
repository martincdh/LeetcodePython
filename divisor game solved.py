n =3
count1 = 0
count2 = 0
m = 1 

while m < n:
    if m ==0 or m%2 !=0:
        count1+=1
    else:
        count2+=1
    m+=1
if count1 > count2:
    print('False')
else:
    print('a')