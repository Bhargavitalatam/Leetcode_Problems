class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        ans=s.count('1')
        ma=0
        lz=0
        i=0
        while i<n:
            o=0
            rz=0
            while i<n and s[i]=='1':
                o+=1
                i+=1
            while i<n and s[i]=='0':
                rz+=1
                i+=1
            if lz and o and rz:
                ma=max(ma,lz+rz)
            lz=rz
        return ans+ma
        