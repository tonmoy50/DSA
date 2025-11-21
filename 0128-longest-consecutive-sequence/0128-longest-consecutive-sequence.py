class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        largest_seq = 0
        for num in s:
            if (num - 1) not in s:
                curr = num
                curr_seq = 1
                while num+curr_seq in s:
                    curr_seq += 1
                    # curr += 1
                largest_seq = max(largest_seq, curr_seq)
        
        return largest_seq