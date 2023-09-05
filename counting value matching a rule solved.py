class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        if ruleKey == 'color':
            index = 1
        elif ruleKey == 'type':
            index =0
        else:
            index = 2

        for i in items:
            if i[index] == ruleValue:
                count+=1
        return count
    
#items[i] = [typei, colori, namei] 
d = {}
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color" #2
ruleValue = "silver"

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"


#ccreating a list of item

item = ['type','color','name']

ruleKey = 'color'
x = item.index(ruleKey)
#x is the index to search for value that equal to ruleValue
