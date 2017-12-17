class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i, x in enumerate(nums):
            if i != x:
                return i
        return i + 1

print(Solution.missingNumber(Solution(), [0]))
print(Solution.missingNumber(Solution(), [1]))
print(Solution.missingNumber(Solution(), [0,1]))
