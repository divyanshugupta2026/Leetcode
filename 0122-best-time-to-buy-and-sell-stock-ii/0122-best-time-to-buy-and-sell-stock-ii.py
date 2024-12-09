class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        a=len(nums)
        profit=0
        for i in range(1,a):
            if(nums[i]>nums[i-1]):
                profit+=nums[i]-nums[i-1]
        return profit