class Solution:
    def trap(self, height: List[int]) -> int:

        greatest_left = [0] * len(height)
        greatest_left[0] = height[0]
        for i in range(1, len(height)):
            greatest_left[i] = max(height[i], greatest_left[i-1])

        greatest_right = [0] * len(height) 
        greatest_right[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            greatest_right[i] = max(height[i], greatest_right[i+1])

        total_water = 0
        for i in range(len(height)):
            total_water += min(greatest_left[i], greatest_right[i]) - height[i]

        return total_water





        