class Solution:
    def isAnagram(self, s, t):
            if len(s) != len(t):
                return False
            alp = [0] * 26
            for i in s:
                alp[ord(i)-97] += 1
            for i in t:
                alp[ord(i)-97] -= 1
                if alp[ord(i)-97] < 0:
                    return False
            return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        else:
            grouped_anagram = []
            marked_idx = [0] * len(strs)
            for i,i_str in enumerate(strs):
                if not marked_idx[i]:
                    grouped_anagram.append([i_str])
                    marked_idx[i] = 1
                    for j in range(i+1, len(strs)):
                        if not marked_idx[j] and self.isAnagram(i_str, strs[j]):
                            grouped_anagram[-1] += [strs[j]]
                            marked_idx[j] = 1
            return grouped_anagram