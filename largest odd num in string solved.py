class Solution(object):
    def largestOddNumber(self, num):
        if int(num) %2 !=0:
            return num
        else:
            a = 0
            num = str(num)
            for j in range(1,len(num)+1):
                if int(num[-j]) %2 != 0:
                    a = len(num) -j+1
                    break
        if a !=0:
            return num[0:a]
        else:
            return ''


#sol 1
check = {"1","3","5","7","9"}
        for i in range(len(num)-1, -1, -1):
            if num[i] in check:
                return num[:i+1]
        return ""


#sol2
for i in range(len(num) - 1, -1, -1) :
            if num[i] in {'1','3','5','7','9'} :
                return num[:i+1]
        return ''