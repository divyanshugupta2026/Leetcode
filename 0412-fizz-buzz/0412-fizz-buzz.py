class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        count=[]
        for i in range(1,n+1):
            if i%5==0 and i%3==0:
                a='FizzBuzz'
                count.append(a)
            elif i%5==0:
                b='Buzz'
                count.append(b)
            elif i%3==0:
                c='Fizz'
                count.append(c)
            else:
                count.append(str(i))
        return count





