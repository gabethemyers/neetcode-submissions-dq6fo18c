class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}

        for n in nums:
            if n in mydict:
                return True
            else:
                mydict[n] = 1
        return False


         