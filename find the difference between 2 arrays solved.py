class Solution(object):
    def findDifference(self, nums1, nums2):
        a = list(set([i for i in nums1 if i not in nums2]))
        b = list(set([j for j in nums2 if j not in nums1]))
        c = [a] + [b]
        return c


#difference function
class Solution(object):
    def findDifference(self, nums1, nums2):

        l1 = list(set(nums2).difference(nums1))
        l2 = list(set(nums1).difference(nums2))
        ls = [l2,l1]

        return ls