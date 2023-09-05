letters = ["f","d","j"]
target = "a"

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        letters = sorted(letters)
        m = letters[0]
        for i in letters:
            if i > target:
                m = i
                break
        return m