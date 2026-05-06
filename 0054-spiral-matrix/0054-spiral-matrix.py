class Solution:
    def spiralOrder(self, ma: List[List[int]]) -> List[int]:
        to=le=0
        bo=len(ma)-1
        ri=len(ma[0])-1
        r=[]
        while to<=bo and le<=ri:
            for i in range(le,ri+1):
                r.append(ma[to][i])
            to+=1
            for i in range(to,bo+1):
                r.append(ma[i][ri])
            ri-=1
            if to<=bo:
                for i in range(ri,le-1,-1):
                    r.append(ma[bo][i])
                bo-=1
            if le<=ri:
                for i in range(bo,to-1,-1):
                    r.append(ma[i][le])
                le+=1
        return r
        