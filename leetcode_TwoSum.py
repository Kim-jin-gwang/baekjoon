class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(1+len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j,i]
    

result = Solution()
nums = list(map(int, input().split()))
target = int(input())
print(result.twoSum(nums, target))
