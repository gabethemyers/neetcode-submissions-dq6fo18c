class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maximum area is the distance between the height indexes, and the min of both heights

        max_area = 0

        left, right = 0, len(heights) - 1

        while left < right:
            curr_area = min(heights[left], heights[right]) * (right - left)

            if curr_area > max_area: max_area = curr_area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return max_area



        