class Solution:
    @staticmethod
    def all_unique(s, i, j):
        ch = set()
        for i in range(i, j):
            if s[i] in ch:
                return False
            ch.update(s[i])
        return True

    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n - 1):
                if self.all_unique(s, i, j):
                    ans = max(ans, j - i)
        return ans

    def sliding_window_length_of_substring(self, s):
        mapping = {chr(i): i for i in range(128)}
        n, ans = len(s), 0
        i = j = 0
        for i in (i, j < n):
            if mapping[s[j]]:
                i = max(mapping[s[j]], i)
            ans = max(ans, j-i+1)
            mapping.update(s[j], j + 1)



a = Solution()
print(a.length_of_longest_substring('abcabcbb'))