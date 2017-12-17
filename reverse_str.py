class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        new = ""
        if string.find('-') != -1:
            string = string.strip('-')
            for x in reversed(string):
                new += x
            if int(new) > 2147483647:
                return 0
            return -int(new)
        else:
            for x in reversed(string):
                new += x
            if int(new) > 2147483647:
                return 0
            return int(new)

a = Solution()
print(a.reverse(567))
print(a.reverse(-567))
