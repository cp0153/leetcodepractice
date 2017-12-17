class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for idx, num in enumerate(nums):
            comp = target - nums[idx]
            if (hash_table.has_key(comp)):
                return [hash_table.get(comp), idx]
            temp = {num: idx}
            hash_table.update(temp)