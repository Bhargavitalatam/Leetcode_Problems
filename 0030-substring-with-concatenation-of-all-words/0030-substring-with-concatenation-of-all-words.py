class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wl=len(words[0])
        tw=len(words)
        tl=wl*tw
        from collections import Counter
        need=Counter(words);r=[]
        for i in range(len(s)-tl+1):
            se=[]
            for j in range(i,i+tl,wl):
                se.append(s[j:j+wl])
            if Counter(se)==need:
                r.append(i)
        return r
