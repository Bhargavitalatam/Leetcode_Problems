class Solution:
    def baseNeg2(self, n: int) -> str:
        ans=""
        if n==0:
            return "0"
        while n:
            n,rem=divmod(n,-2)
            if rem<0:
                rem+=2
                n+=1
            ans+=str(rem)
        return ans[::-1]
        