import numpy as np
class Solution:
    def is_duplicate(self, nums: List[int]) -> bool:
        print(nums)
        numset = set()
        for num in nums:
            if num in numset:
                return True
            else:
                numset.add(num) if num != "." else numset
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # print(board[:][0])
        board = np.array(board)
        # print(board)
        for i,row in enumerate(board):
            if self.is_duplicate(board[i, :]):
                print("Ekhane1")
                return False
            if self.is_duplicate(board[:, i]):
                print("Ekhane2")
                return False
        for i in range(0, 9, 3):
            # print(board)
            if self.is_duplicate(board[i:i+3, :3].flatten()):
                print("Ekhane3", i)
                return False
            if self.is_duplicate(board[i:i+3, 3:6].flatten()):
                print("Ekhane4")
                return False
            if self.is_duplicate(board[i:i+3, 6:9].flatten()):
                print("Ekhane5")
                return False
        return True
        