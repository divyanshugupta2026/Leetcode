class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        a=len(nums)
        l=0
        r=k
        c_sum=sum(nums[:k])
        max_avg= c_sum/float(k)
        for i in range(k,a):
            c_sum+=nums[i]
            c_sum-=nums[i-k]
            avg=c_sum/float(k)
            max_avg=max(max_avg,avg)
        return max_avg
        