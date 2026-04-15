class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      diction = dict()
      for num in nums:
        if num in diction:
          diction[num] += 1
        else:
          diction[num] = 1
      sorted_freq = sorted(diction.items(), key=lambda x: x[1], reverse=True)
      result = [x[0] for x in sorted_freq]
      return result[:k]
     
