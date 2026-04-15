class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      diction = dict()
      for num in nums:
        diction[num] = diction.get(num, 0) + 1
      sorted_freq = sorted(diction.items(), key=lambda x: x[1], reverse=True)[:k]
      return [x[0] for x in sorted_freq]
     
     
