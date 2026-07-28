class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        fre=[0]*26
        for i in s:
            fre[ord(i)-ord('a')]+=1
        l=0;r=len(s)-1
        a=['']*n 
        for i in range(26):
            while fre[i]>=2:
                a[l]=chr(ord('a')+i)
                a[r]=chr(ord('a')+i)
                l+=1
                r-=1
                fre[i]-=2
            if fre[i]==1:
                a[n//2]=chr(ord('a')+i)
        return ''.join(a)
        