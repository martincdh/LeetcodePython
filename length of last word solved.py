class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for i in range(1,len(s) +1):
            if s[-i] != ' ':
                count+=1
            if (count > 0) and s[-i] == ' ' or i == len(s):
                return count
                break

s = "   fly me   to   the moon  "
s = "luffy is still joyboy"
s = 'a'