class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            lptr, rptr = i+1, len(nums)-1
            while lptr < rptr:
                total = a + nums[lptr] + nums[rptr]
                if total > 0:
                    rptr -= 1
                elif total < 0:
                    lptr += 1
                else:
                    res.append([a, nums[lptr], nums[rptr]])
                    lptr += 1
                    while (nums[lptr] == nums[lptr - 1]) and lptr < rptr:
                        lptr += 1
        
        return res