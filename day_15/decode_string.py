class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        cur = ""
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                continue

            if c == '[':
                stack.append((num, cur))
                cur = ""
                num = 0
                continue

            if c == ']':
                _t = stack.pop()
                cur = _t[1] + _t[0] * cur
                continue

            cur = cur + c

        return cur

print(Solution().decodeString("3[a2[c2[f]d]]"))