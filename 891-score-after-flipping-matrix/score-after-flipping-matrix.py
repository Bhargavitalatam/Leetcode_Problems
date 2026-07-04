class Solution:
    def cal(self,grid):
        r=len(grid);c=len(grid[0])
        s=0
        for i in range(r):
            x=1
            for j in range(c-1,-1,-1):
                if grid[i][j]==1:
                    s+=x
                x*=2
        return s
    def colflip(self,grid,i):
        for k in range(len(grid)):
            grid[k][i]^=1
    def matrixScore(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        for i in range(n):
            if grid[i][0]==0:
                for j in range(m):
                    grid[i][j]^=1
        for i in range(m):
            c0=c1=0
            for j in range(n):
                if grid[j][i]==0:
                    c0+=1
                else:
                    c1+=1
            if c0>c1:
                self.colflip(grid,i)
        return self.cal(grid)

        