class Solution(object):
    def compress(self, char):
        """
        :type chars: List[str]
        :rtype: int
        """
        a=len(char)
        count=1
        out=""
        for i in range(a):
            if i + 1 < a and char[i] == char[i + 1]:
                count += 1
            else:
                out+=str(char[i])
                if count>1:
                    out+=str(count)
                count=1
        for i in range(len(out)):
            char[i] = out[i]
        return len(out)

