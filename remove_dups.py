class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        for i, num in enumerate(nums):
            first = nums[i]
            second = nums[i + 1] if len(nums) > i+1 else -1
            if first == second:
                nums.pop(i)
        return len(nums)

a = Solution()
liste = [i for i in range(10)]
liste.append(9)
print liste
print a.removeDuplicates(liste)
print a.removeDuplicates([1,1,1])