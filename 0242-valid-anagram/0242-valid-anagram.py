class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            alp = [0] * 26
            for i in s:
                alp[ord(i)-97] += 1
            for i in t:
                alp[ord(i)-97] -= 1
                if alp[ord(i)-97] < 0:
                    return False
            return True


        