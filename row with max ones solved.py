class Solution(object):
    def rowAndMaximumOnes(self, mat):
        max_s = 0
        y=0
        for i in mat:
            x = i.count(1)
            if x > max_s:
                max_s = x
                y = mat.index(i)
        return [y,max_s]
    
Input: mat = [[0,1],[1,0]]
Output: [0,1]

Input: mat = [[0,0,0],[0,1,1]]
Output: [1,2]

Input: mat = [[0,0],[1,1],[0,0]]
Output: [1,2]