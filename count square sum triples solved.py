class Solution(object):
    def countTriples(self, n):
        count = 0
        for a in range(1,n+1):
            for b in range(a+1,n+1):
                for c in range(b+1,n+1):
                    if a**2 + b**2 == c**2:
                        count +=1
        return count*2
    
#sol1
counts = 0
        for a in range(1,n):
            for b in range(a+1,n):
                c = math.sqrt(a**2 + b**2)
                if int(c)==c and c<=n:
                    counts +=2
        return counts

#sol2 creating a set()
class Solution:
  def countTriples(self, n):
    ans = 0
    squared = set()

    for i in range(1, n + 1):
      squared.add(i * i)  #creating set with pow of 2

    for a in squared: 
      for b in squared:
        if a + b in squared: #check sum a+b in squared because 'C' already in the square
          ans += 1   # counting

    return ans