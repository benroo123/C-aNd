# two sum
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pass

class TwoSum:
    # solution one
    # simply uses the 2d for loop
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # print(i, j)
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [0, 0]

    # an advanced version
    # uses loop unrolling
    def advTwoSum(self, nums, target):
        # length = len(nums) // 2 + 1
        i = 0
        while i <= len(nums) - 1:
            j = i + 1
            k = len(nums) - 1
            while j <= len(nums) - 1:
                print(i, j, k)
                if nums[i] + nums[j] == target:
                    return [i, j]
                if nums[i] + nums[k] == target:
                    return [i, k]
                j += 1
                k -= 1
            i += 1

        return [0, 0]


if __name__ == "__main__":
    t = TwoSum()
    print(t.twoSum([3, 3], 6))
    print(t.advTwoSum([2, 7, 11, 15], 18))
