class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        else:
            diffmap = dict()
            for i,num in enumerate(nums):
                diff = target - num
                if str(diff) in diffmap:
                    return [diffmap[str(diff)], i]
                diffmap[str(num)] = i