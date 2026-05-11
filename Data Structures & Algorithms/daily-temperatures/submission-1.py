class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force would be two for loops to compare every future temp to the current
        # 
        
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            curr_temp = temperatures[i]
            while stack and curr_temp > temperatures[stack[-1]]:
                temp_index = stack.pop()

                ans[temp_index] = i - temp_index
            
            stack.append(i)

        return ans
                    



