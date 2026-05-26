class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search for the row:

        row_right = len(matrix) - 1
        row_left = 0
        row_mid = row_right // 2

        while row_left <= row_right:
            row_mid = (row_left+row_right) // 2
            
            if target < matrix[row_mid][0]:
                row_right = row_mid - 1
            elif target > matrix[row_mid][-1]:
                row_left = row_mid + 1
            else:
                break

        
        target_row = matrix[row_mid]
        left = 0
        right = len(target_row) - 1
        mid = right // 2

        while left <= right:
            mid = (left + right) // 2
            if target < target_row[mid]:
                right = mid - 1
            elif target > target_row[mid]:
                left = mid + 1
            else:
                return True

        return False 

        

