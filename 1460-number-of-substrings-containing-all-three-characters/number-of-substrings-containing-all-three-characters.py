class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        p=[-1,-1,-1]
        res=0
        for i,j in enumerate(s):
            p[ord(j)-ord('a')]=i
            res+=min(p)+1
        return res
        