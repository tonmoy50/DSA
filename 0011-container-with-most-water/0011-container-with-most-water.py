class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        lptr, rptr = 0, len(height) -1

        while lptr < rptr:
            area = max(area, (rptr - lptr) * min(height[lptr], height[rptr]))
            if height[lptr] < height[rptr]:
                lptr += 1
            else:
                rptr -= 1
        
        return area