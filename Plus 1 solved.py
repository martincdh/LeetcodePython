
def plusOne(digits):
        m = 0 
        for i in digits:
            m = m*10 + i
        m = m+1
        a = [int(x) for x in str(m)]
        return a

print(plusOne(digits = [1,2,3,10]))
1230+10