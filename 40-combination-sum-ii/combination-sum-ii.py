class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        r=[]
        c.sort()
        def dfs(ind,pa,cur):
            if cur>target:
                return
            if cur==target:
                r.append(pa)
                return
            for i in range(ind,len(c)):
                if i>ind and c[i]==c[i-1]:
                    continue
                dfs(i+1,pa+[c[i]],cur+c[i])
        dfs(0,[],0)
        return r                

        