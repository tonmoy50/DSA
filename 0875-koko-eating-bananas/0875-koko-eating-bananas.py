class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        
        min_k = max_pile
        l, r = 1, max_pile
        
        while l <= r:
            mid = (l+r)//2
            total_hours = 0
            for pile in piles:
                if pile >= mid:
                    total_hours += (pile//mid) + (1 if pile%mid > 0 else 0)
                else:
                    total_hours += 1
            if total_hours <= h:
                min_k = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return min_k