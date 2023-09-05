grid = [[3,2],[1,0]]
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
class Solution(object):
    def countNegatives(self, grid):
        m = 0
        for i in grid:
            c = 0
            for j in i:
                if j <0:
                    c+=1
            m+=c
        return m
        print(m)
    