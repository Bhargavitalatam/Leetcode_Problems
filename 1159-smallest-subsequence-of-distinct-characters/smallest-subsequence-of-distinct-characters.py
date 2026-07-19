class Solution:
    def smallestSubsequence(self, s: str) -> str:
        l={}
        for i,v in enumerate(s):
            l[v]=i
        st=[];vi=set()
        for i,v in enumerate(s):
            if v in vi:
                continue
            while(st and st[-1]>v and l[st[-1]]>i):
                vi.remove(st.pop())
            st.append(v)
            vi.add(v)  
        return "".join(st)      