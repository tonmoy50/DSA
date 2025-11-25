class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        lptr, rptr = 0, len(height) - 1
        maxL, maxR = height[lptr], height[rptr]

        while lptr != rptr:
            if maxL <= maxR:
                lptr += 1
                if maxL - height[lptr] > 0:
                    total_water += maxL - height[lptr]
                maxL = max(maxL, height[lptr])
            else:
                rptr -= 1
                if maxR - height[rptr] > 0:
                    total_water += maxR - height[rptr]
                maxR = max(maxR, height[rptr])
        
        return total_water