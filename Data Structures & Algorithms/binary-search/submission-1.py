class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        mid = len(nums) // 2
        right = len(nums) - 1

        while (nums[mid] != target):
            if left > right:
                return -1
            if nums[mid] > target:
                right = mid - 1
                mid = (right + left) // 2
            else:
                left = mid + 1
                mid = (right + left) // 2

        return mid
        