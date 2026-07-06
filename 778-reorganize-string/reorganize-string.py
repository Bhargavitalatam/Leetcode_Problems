class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        c=Counter(s)
        if max(c.values())>(len(s)+1)//2:
            return ""
        a=[(-co,ch) for ch,co in c.items()]
        import heapq
        heapq.heapify(a)
        ans=[]
        while len(a)>1:
            co1,ch1=heapq.heappop(a)
            co2,ch2=heapq.heappop(a)
            ans.append(ch1)
            ans.append(ch2)
            co1+=1
            co2+=1
            if co1<0:
                heapq.heappush(a,(co1,ch1))
            if co2<0:
                heapq.heappush(a,(co2,ch2))
        if a:
            ans.append(a[0][1])
        return "".join(ans)        