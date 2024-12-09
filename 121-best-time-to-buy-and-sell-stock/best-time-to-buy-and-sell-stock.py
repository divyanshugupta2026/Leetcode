class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p=nums[0]
        max_profit=0
        a=len(nums)
        for i in range(a):
            if nums[i]<min_p:
                min_p=nums[i]
            else:
                a=nums[i]-min_p
                max_profit= max(a,max_profit)
        return max_profit




