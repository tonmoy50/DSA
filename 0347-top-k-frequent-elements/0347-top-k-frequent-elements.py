import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        k_keys_sorted = heapq.nlargest(k, freq_dict, key=freq_dict.get)
        return k_keys_sorted