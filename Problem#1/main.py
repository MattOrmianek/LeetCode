class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for i, value in enumerate(nums):
            searched_value = target - nums[i]

            if searched_value in seen:
                return [seen[searched_value],i]
            else:
                seen[value] = i