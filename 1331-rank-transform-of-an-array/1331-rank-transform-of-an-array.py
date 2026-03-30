class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(set(arr))
        r=[];d={}
        for i in range(len(s)):
            d[s[i]]=i+1
        for i in arr:
            r.append(d[i])
        return r
        