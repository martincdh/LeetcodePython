def kidsWithCandies(candies, extraCandies):
    for i in range(len(candies)):
        candies[i] += extraCandies
        max_a = candies[i]
        for n in range(len(candies)):
            if candies[n] < max_a:
                print(max_a)
    print(candies)


kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)


wordsDict = ["a","a","b","b"]
word1 = "a"
word2 = "b"

for i in range(len(wordsDict)):
    if wordsDict[i] == word1:
        x = i
        print(i)
for j in range(len(wordsDict)):
    if wordsDict[j] == word2:
        y = j
        print(j)

dist = abs(j-i)
print(dist)



nums = [1,1,0,-1]
x = min(nums)

print(x)

nums = sorted(nums)
nums = list(set(nums))
x= []
for i in range(len(nums)):
    if i+1 != nums[i]:
        x.append(i+1)

print(x)

a = num = 199
a = str(a)
c = 0
while len(a) > 1:
    for i in range(len(a)):
        c+= int(a[i])
    
    a = str(c)
    c=0
    

while num >= 10:
            num = sum(int(i) for i in str(num))
        return num


print(a)