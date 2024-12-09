class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=len(nums)
        out=[]
        for i in range(a):
            mult=1
            for j in range(a):
                if(i==j):
                    continue
                else:
                    mult*=nums[j]
            out.append(mult)
        return out
            