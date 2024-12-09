class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pref=1
        suff=1
        a=len(nums)
        out=[1]*a
        for i in range(a):
            out[i]=pref
            pref*=nums[i]
        for j in range(a-1,-1,-1):
            out[j]*=suff
            suff*=nums[j]
        return out
            

            