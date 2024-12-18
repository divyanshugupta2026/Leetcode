class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel=['a','e','i','o','u']
        l=0
        count1=[]
        count2=0
        a=len(s)
        for i in range(a):
            if s[i] in vowel:
                count2 += 1
            if i >= k - 1:
                count1.append(count2)
                if s[l] in vowel:
                    count2 -= 1
                l+=1
            
        return max(count1)