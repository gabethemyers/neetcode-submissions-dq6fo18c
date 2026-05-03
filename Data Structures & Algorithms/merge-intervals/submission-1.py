class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # keep track of the minimum value, and the maximum then check each start end merges
        intervals.sort(key=lambda x: x[0])
        

        result = []

        for i, interval in enumerate(intervals):
            if i == 0:
                result.append(interval)
                continue
            last_policy = result[-1]
            if last_policy[1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        
        return result
                
            