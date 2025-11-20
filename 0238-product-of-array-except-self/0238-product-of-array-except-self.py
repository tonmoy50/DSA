class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_prod = 1
        total_zero = 0
        for num in nums:
            if num != 0:
                res_prod *= num
            else:
                total_zero += 1
                zero_flag = 1
        if total_zero > 1:
            return [0] * len(nums)

        output = [0] * len(nums)
        for i,num in enumerate(nums):
            if total_zero: 
                if num:
                    output[i] = 0 
                else:
                    output[i] = res_prod
            else:
                output[i] = res_prod // num
        return output