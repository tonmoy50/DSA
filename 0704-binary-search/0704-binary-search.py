class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_tree(l, r, arr, target):
            if l > r:
                return -1
            
            m = l + (r - l) // 2

            if arr[m] == target:
                return m
            elif arr[m] < target:
                return search_tree(m+1, r, arr, target)
            else:
                return search_tree(l, m-1, arr, target)

        return search_tree(0, len(nums)-1, nums, target)