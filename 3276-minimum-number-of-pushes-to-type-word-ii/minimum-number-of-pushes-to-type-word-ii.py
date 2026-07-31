class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        p=Counter(word)
        s=sorted(p.values(),reverse=True)
        r=0
        for i,j in enumerate(s):
            r+=(i//8+1)*j
        return r            
        