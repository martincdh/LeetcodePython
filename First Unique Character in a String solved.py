class Solution(object):
    def firstUniqChar(self, s):
        c = -1
        for i in range(len(s)):
            x = s.count(s[i])
            if x ==1:
                c = i
                break
        return c

for letter in s:
            # rindex last occurance of the index
            # index first occurance of the index
            if s.rindex(letter) == s.index(letter):
                return s.index(letter)
        return -1

class Solution(object):
    def firstUniqChar(self, s):
        abc = "abcdefghijklmnopqrstuvwxyz"
        ans = 10 ** 5  # since 1 <= s.length <= 105, the answer must be smaller than 10^5
        print(s.find('e'))
        for c in abc:
            idx = s.find(c)  # check if this word is in s
            if (idx != -1 and idx == s.rfind(c)):  # check if first index == last index
                ans = min(ans, idx)  # store the smallest 

        return ans if ans < 10 ** 5 else -1
    
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {}
        for letter in s:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        for letter in s:
            if dictionary[letter] == 1:
                return s.index(letter)
        return -1