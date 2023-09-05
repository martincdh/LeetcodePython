class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        c =''
        d=''
        for i in word1:
            c+=i
        for j in word2:
            d+=j
        if c == d:
            return True
        else:
            return False
        
word1 = ["ab", "c"]
word2 = ["a", "bc"]