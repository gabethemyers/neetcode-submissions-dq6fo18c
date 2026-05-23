class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}

        for i, num in enumerate(nums):
            compliment = target-num
            if compliment in diction:
                return [diction[compliment], i]
            else:
                diction[num] = i
        

        