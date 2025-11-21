class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list()
        for i in range(len(s)):
            if (
                (ord(s[i]) >= 48 and ord(s[i]) <= 57) or 
                (ord(s[i]) >= 65 and ord(s[i]) <= 90) or 
                (ord(s[i]) >= 97 and ord(s[i]) <= 122)
            ):
                chars.append(s[i].lower())
        
        end_pointer = len(chars) - 1
        for i in range(math.ceil(len(chars) / 2)):
            if chars[i] != chars[end_pointer]:
                return False
            else:
                end_pointer -= 1
        return True