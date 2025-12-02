class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m - 1
        while top <= bottom:
            mid_m = (top+bottom) // 2
            if target > matrix[mid_m][-1]:
                top = mid_m + 1
            elif target < matrix[mid_m][0]:
                bottom = mid_m - 1
            else:
                break
        
        if top > bottom:
            return False
        
        mid_m = (top+bottom) // 2
        lptr, rptr = 0, n - 1
        while lptr <= rptr:
            mid_n = (lptr+rptr) // 2
            if target > matrix[mid_m][mid_n]:
                lptr = mid_n + 1
            elif target < matrix[mid_m][mid_n]:
                rptr = mid_n - 1
            else:
                return True
        
        return False