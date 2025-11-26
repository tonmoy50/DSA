class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        symbols = set()
        l = 0
        longest_substring = 0

        for r in range(len(s)):
            while s[r] in symbols:
                symbols.remove(s[l])
                l += 1
            symbols.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)
        
        return longest_substring