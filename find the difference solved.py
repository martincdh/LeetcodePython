class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if s.count(i) != t.count(i):
                return i
                break

#amazon, IBM and Google question