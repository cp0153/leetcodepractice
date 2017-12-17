def counts(nums, maxes):
    ans = []
    for max_val in maxes:
        count = 0
        for num in nums:
            if num <= max_val:
                count += 1
        ans.append(count)
    return ans
