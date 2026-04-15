class Solution:
    def trap(self, height: List[int]) -> int:
        # need to precomute the greater elements to the left and right of each index.
        # to find the greater elements on each side i need to make sure that the height is increasing or the same height
        # left array for the greatest element to the left and vis versa for right

        greatest_left = [0] * len(height)
        greatest_right = [0] * len(height)

        for i, curr_height in enumerate(height):
            max_left = curr_height
            l_pointer = i
            while l_pointer > 0:
                max_left = max(max_left, height[l_pointer-1])
                l_pointer -= 1
            greatest_left[i] = max_left

            max_right = curr_height
            r_pointer = i
            while r_pointer < len(height) - 1:
                max_right = max(max_right, height[r_pointer + 1])
                r_pointer += 1
            greatest_right[i] = max_right
        
        total_water = 0

        for i in range(len(greatest_left)):
            total_water += min(greatest_left[i], greatest_right[i]) - height[i]
        
        return total_water








        