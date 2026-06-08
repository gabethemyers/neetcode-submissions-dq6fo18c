class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        max_length = 0

        for num in nums:
            if (num - 1) not in set_nums:
                seq_num = num
                seq_length = 0
                while seq_num in set_nums:
                    seq_num += 1
                    seq_length += 1

                max_length = max(max_length, seq_length)

        return max_length 