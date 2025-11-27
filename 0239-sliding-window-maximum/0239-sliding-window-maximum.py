class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        res = list()
        max_heap = collections.deque()
        
        while r < len(nums):
            while max_heap and nums[max_heap[-1]] < nums[r]:
                max_heap.pop()
            max_heap.append(r)

            if l > max_heap[0]:
                max_heap.popleft()
            
            if (r+1) >= k:
                res.append(nums[max_heap[0]])
                l += 1
            r+= 1

        return res