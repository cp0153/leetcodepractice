class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i, x in enumerate(nums):
            if x == target:
                result.append(i)
        if len(result) > 2:
            return [result[0], result[-1]]
        if not result:
            return [-1, -1]
        if len(result) == 2:
            return result

a = Solution()
print(a.searchRange([5,7,7,8,8,10], 8))