class Solution:
    def is_palindrome_n_space(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    def is_palindrome_log_space(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x != 0 and x % 10 == 0:
            return False
        else:
            sum = 0
            while x > sum:
                sum = sum * 10 + x % 10
                x = x / 10
            return x == sum or x == sum / 10

