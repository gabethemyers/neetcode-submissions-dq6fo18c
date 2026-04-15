class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to get o(1) lookup times

        set_of_nums = set(nums)

        longest = 0

        for num in nums:
            if (num - 1) not in set_of_nums:
                # start building a squence 
                start = num
                curr_longest = 1
                while True:
                    start += 1
                    if start not in set_of_nums:
                        break
                    curr_longest += 1
                if curr_longest > longest:
                    longest = curr_longest

        return longest