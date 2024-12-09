class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=s.split()
        b=len(count)
        a=[]
        for i in range(b-1,-1,-1):
            a.append(count[i])     
        return " ".join(a)