class Solution:
    def stoneGameIII(self, s: List[int]) -> str:
        n=len(s)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            ta=0
            dp[i]=float('-inf')
            for j in range(3):
                if i+j<n:
                    ta+=s[i+j]
                    dp[i]=max(dp[i],ta-dp[i+j+1])
        if dp[0]>0:
            return "Alice"
        elif dp[0]<0:
            return "Bob"
        return "Tie"

        