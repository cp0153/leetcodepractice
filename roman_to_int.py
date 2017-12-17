class Solution(object):
    def char_to_num(self, char):
        if char == 'I':
            return 1
        elif char == 'V':
            return 5
        elif char == 'X':
            return 10
        elif char == 'L':
            return 50
        elif char == 'C':
            return 100
        elif char == 'D':
            return 500
        elif char == 'M':
            return 1000
        else:
            return -1

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        while s:
            first = self.char_to_num(s[0])
            second = self.char_to_num(s[1]) if len(s) > 1 else -1
            if first >= second:
                val += first
                s = s[1:]
            else:
                val += second - first
                s = s[2:]
        return val





a = Solution()
print a.romanToInt('DCXXI')
print a.romanToInt('DCXXI')
print a.romanToInt('DCXXI')
print a.romanToInt('MCMXCVI')
print a.romanToInt('MCM')
print a.romanToInt('MMC')
print a.romanToInt('XXM')

