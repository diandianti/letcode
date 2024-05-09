def check(s:dict, t:dict) -> bool:
    for k,v in t.items():
        if s.get(k, 0) < v:
            return False

    return True

class Solution:


    def minWindow(self, s: str, t: str) -> str:
        win = {}
        tar = {}
        for c in t:
            tar[c] = tar.get(c, 0) + 1

        l,r = 0, 0
        ll = len(s)

        _min = ll
        _mins = ""
        while r < ll:
            while r < ll and not check(win, tar):
                win[s[r]] = win.get(s[r], 0) + 1
                r += 1


            while l < r and check(win, tar):
                win[s[l]] -= 1
                l += 1

            if _min > (r - l):
                _min = (r - l)
                _mins = s[l - 1: r]

        return _mins

print(Solution().minWindow("a", "a"))
