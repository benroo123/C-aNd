# two sum
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pass

class TwoSum:

    def twoSum(self, nums, target):
        result = [0, 0]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                print(i, j)
                if nums[i] + nums[j] == target:
                    result[0], result[-1] = i, j
                    break

        return result


t = TwoSum()
print(t.twoSum([3, 3], 6))
