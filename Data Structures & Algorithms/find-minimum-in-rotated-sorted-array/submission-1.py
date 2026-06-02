class Solution:
    def findMin(self, nums: List[int]) -> int:
        # it is still sorted but not "in order"
        left = 0
        right = len(nums) - 1

        mini = 1001

        while left <= right:
            mid = (left + right) // 2
            # if right is < left than I know the array was rotated

            # maybe I should compare left and right to see where to move mid?
            mini = min(mini, nums[mid])
            if nums[left] > nums[right]:
                left += 1
            else:
                right = mid - 1
        return mini
            

        
        