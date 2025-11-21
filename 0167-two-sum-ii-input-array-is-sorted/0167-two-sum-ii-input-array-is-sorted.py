class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr = 0
        rptr = len(numbers) - 1
        while (numbers[lptr] + numbers[rptr]) != target:
            if (numbers[lptr] + numbers[rptr]) > target:
                rptr = rptr - 1
            elif (numbers[lptr] + numbers[rptr]) < target:
                lptr += 1
        
        return [lptr+1, rptr+1]