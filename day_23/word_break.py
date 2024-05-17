from typing import List, Dict

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dp: Dict[str, bool] = {}
        self.wd = wordDict

        for w in self.wd:
            self.dp[w] = True

        def recur2(ss: List[str], origin_s: str):
            if origin_s in self.dp:
                return self.dp[origin_s]

            if len(ss) == 1 and ss[0] in self.wd:
                return True
            if len(ss) == 1 and ss[0] == origin_s:
                return False

            all_same = True
            for i in ss:
                if i != '':
                    all_same = False
            if all_same:
                return True

            flag = True
            for s in ss:
                if s == '':
                    continue
                flag = flag and recur1(s)

            return flag

        def recur1(ins: str):
            flag = False
            for w in self.wd:
                ss = ins.split(w)
                flag = flag or recur2(ss, ins)

            self.dp[ins] = flag
            return flag

        return recur1(s)


print(Solution().wordBreak(s = "bb", wordDict = ["a","b","bbb","bbbb"]))