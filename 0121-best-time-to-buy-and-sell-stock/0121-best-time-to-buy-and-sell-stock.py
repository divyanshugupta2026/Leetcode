class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        a=len(prices)
        day=0
        lowp = float('inf')
        for i in range(a):
            if prices[i]<lowp:
                lowp=prices[i]
                day=i
            else:
                i+=1
        profit=[]
        for c in range(day, a):
            if prices[c] > lowp:
                profit.append(prices[c] - lowp)

        if profit:
            return max(profit)
        else:
            return 0



