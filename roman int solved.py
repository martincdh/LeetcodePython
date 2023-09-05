def romanToInt(s):
        d = 0
        i=0
        for i in range(len(s)):
            if i == 0:
                if s[i] == 'I':
                    d+=1
                if s[i] =='V':
                    d+=5
                if s[i] =='X':
                    d+=10
                if s[i] == 'L':
                    d+=50
                if s[i] =='C':
                    d+=100
                if s[i] =='D':
                    d+=500
                if s[i] =='M':
                    d+=1000
            else:
                    if s[i] == 'I':
                        d+=1
                    if i!=0 and s[i] == 'V' and s[i-1] != 'I':
                        d+=5
                    elif s[i] == 'V' and s[i-1] == 'I':
                        d+=3
                    if s[i] == 'X' and s[i-1] != 'I':
                        d+=10
                    elif s[i] == 'X' and s[i-1] == 'I':
                        d+=8
                    if s[i] == 'L' and s[i-1] != 'X':
                        d+=50
                    elif s[i] =='L' and s[i-1] =='X':
                        d+=30
                    if s[i] == 'C' and s[i-1] != 'X':
                        d+=100
                    elif s[i] == 'C' and s[i-1] == 'X':
                        d+=80
                    if s[i] == 'D' and s[i-1] != 'C':
                        d+=500
                    elif s[i] == 'D' and s[i-1] == 'C':
                        d+=300
                    if s[i] == 'M' and s[i-1] != 'C':
                        d+=1000
                    elif s[i] == 'M' and s[i-1] == 'C':
                        d+=800
                
        print(d) 

romanToInt(s = 'MCDLXXVI')



class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = {} 
        l["I"] = 1 
        l["V"] = 5
        l["X"] = 10
        l["L"] = 50
        l["C"] = 100
        l["D"] = 500
        l["M"] = 1000

        count = 0

        i = len(s)-1

        p = 0

        while(i >= 0):

            n = l[s[i]]

            if n < p:
                count -= n
            else:
                count += n
                p = n 

            
            i -= 1

        
        return count 