class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force would be two for loops to compare every future temp to the current
        # 
        

        stack = [0]
        answers = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]

            if curr_temp <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                print(stack)
                while len(stack) > 0 and temperatures[stack[-1]] < curr_temp:
                    # pop and place the difference between i and popped result into answers
                    temp_index = stack.pop()
                    answers[temp_index] = i - temp_index
                stack.append(i)
            
        return answers
                    



