from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in temp:
                temp[k].append(s)
            else:
                temp[k] = [s]

        res = []
        for _,v in temp.items():
            res.append(v)
        return res

class Solution2:

    def hash_help(self, ss):
        res = [0] * 26
        for s in ss:
            res[ord(s) - ord('a')] += 1
        return str(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for s in strs:
            k = self.hash_help(s)
            if k in temp:
                temp[k].append(s)
            else:
                temp[k] = [s]

        res = []
        for _,v in temp.items():
            res.append(v)
        return res


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    s = Solution2()
    print(s.groupAnagrams(strs))