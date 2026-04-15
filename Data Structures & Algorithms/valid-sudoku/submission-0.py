from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            dupl = set()
            for num in row:
                if num == ".":
                    continue
                elif num in dupl:
                    return False
                else:
                    dupl.add(num)
            


        #columns
        for x in range(len(board)):
            dupl = set()
            for y in range(len(board)):
                num = board[y][x]
                if num == ".":
                    continue
                elif num in dupl:
                    return False
                else:
                    dupl.add(num)


        #squares
        # i need a hash set with 9 keys being the square nums

        square_sets = defaultdict(set)

        for x in range(len(board)):
            for y in range(len(board)):
                key = (x // 3) * 3 + (y // 3)
                num = board[x][y]
                print(key, num)
                if num == ".":
                    continue
                elif num in square_sets[key]:
                    print(square_sets)
                    return False
                else:
                    square_sets[key].add(num)
        

        


        return True