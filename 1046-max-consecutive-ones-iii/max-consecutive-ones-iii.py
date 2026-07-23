class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        l=r=0
        for r in range(len(a)):
            if a[r]==0:
                k-=1
            if k<0:
                if a[l]==0:
                    k+=1
                l+=1
        return r-l+1