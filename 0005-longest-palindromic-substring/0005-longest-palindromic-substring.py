class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        r=""
        for i in range(n):
            le,ri=i,i+1
            while le>=0 and ri<n and s[le]==s[ri]:
                if len(r)<ri-le+1:
                    r=s[le:ri+1]
                le-=1
                ri+=1
            le,ri=i,i
            while le>=0 and ri<n and s[le]==s[ri]:
                if len(r)<ri-le+1:
                    r=s[le:ri+1]
                le-=1
                ri+=1
        return ''.join(r)
            
        