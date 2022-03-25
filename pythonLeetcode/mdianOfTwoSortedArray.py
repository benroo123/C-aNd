# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
def c(a, b):
    alist = []
    if a == [] and b == []:
        return alist
    if a != [] and b == []:
        return alist + a
    if a == [] and b != []:
        return alist + b
    if a != [] and b != []:
        if a[0] <= b[0]:
            alist.append(a[0])
            alist = alist + c(a[1:], b)
        if a[0] > b[0]:
            alist.append(b[0])
            alist = alist + c(a, b[1:])
    return alist

class Solution:
    def combine(self, nums1, nums2) -> list:
        together = []
        if nums1 == [] and nums2 == []:
            return together
        elif not nums1:
            return together + nums2
        elif not nums2:
            return together + nums1

        else:
            if nums1[0] <= nums2[0]:
                # nums1[0]
                print(nums1[0])
                together = (together.append(nums1[0])).extend(Solution.combine(self, nums1[1:], nums2))
            elif nums1[0] > nums2[0]:
                # nums2[0]
                print(nums2[0])
                together = together.append(nums1[0]) + Solution.combine(self, nums1, nums2[1:])
            return together

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num = c(nums1, nums2)
        length = len(num) - 1
        print(length)
        if length % 2 == 0:
            return num[length // 2]
        else:
            return (num[length // 2] + num[length // 2 + 1]) / 2


if __name__ == "__main__":
    s = Solution()
    t1 = [1, 3, 5, 7, 9, 11]
    t2 = [3, 8, 9, 10, 20, 25, 30]
    s.combine(t1, t2)
    # print(c(t1, t2))