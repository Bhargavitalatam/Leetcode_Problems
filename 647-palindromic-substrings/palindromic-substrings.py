class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        c=0
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1]==s[i:j+1][::-1]:
                    c+=1
                
        return c

        