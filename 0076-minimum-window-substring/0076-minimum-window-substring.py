class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        count_t, win = dict(), dict()

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        have, need = 0, len(count_t)
        min_win, min_win_length = [0, 0], float("infinity") 
        l = 0
        for r in range(len(s)):
            win[s[r]] = 1 + win.get(s[r], 0)

            if s[r] in count_t:
                if win[s[r]] == count_t[s[r]]:
                    have += 1
            
            while have == need:
                if (r-l+1) < min_win_length:
                    min_win = [l, r]
                    min_win_length = r-l+1
                win[s[l]] -= 1
                if s[l] in count_t:
                    if win[s[l]] < count_t[s[l]]:
                        have -= 1
                l += 1
            
        l = min_win[0]
        r = min_win[1]

        return s[l:r+1] if min_win_length != float("infinity") else ""