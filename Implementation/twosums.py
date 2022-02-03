class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                if (nums[i] + nums[j]) == target:
                    result.append(i)
                    result.append(j)
                    return result

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

sol = Solution()
nums=[3,3]
target=6
print(sol.twoSum(nums,target))