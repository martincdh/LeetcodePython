class Solution(object):
    def numberOfDays(self, year, month):
        
        if month in (1,3,5,7,8,10,12):
            return 31
        elif month in (4,6,9,11):
            return 30
        elif year%4 ==0 and month ==2:
            if year%100 ==0:
                if year%400 == 0:
                    return 29
                else:
                    return 28
            else:

                return 29
        else:
            return 28