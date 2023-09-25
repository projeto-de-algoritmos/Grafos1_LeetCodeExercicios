from collections import deque

class Solution:
    """
        :type grid: List[List[int]]
        :rtype: int
    """
    def shortestBridge(self, grid):
        n = len(grid)
        direcoes = [[1,0], [-1,0], [0,1], [0,-1]]
        
        visitados = set()
    
        def erro(l, c):
            return l < 0 or c < 0 or l == n or c == n
           

        def dfs(l, c):    
            if (erro(l, c) or not grid[l][c] or (l, c) in visitados):
                return
            visitados.add((l, c))   
            for dc, dl in direcoes:
                dfs(l + dl, c + dc)

        def bfs():
            res, queue = 0, deque(visitados)
            while queue:
                for i in range(len(queue)):
                    l, c, = queue.popleft()
                    for dl, dc in direcoes:
                        al, ac =  l + dl, c + dc
                        if erro(al, ac) or (al, ac) in visitados:
                            continue
                        if grid[al][ac]:
                            return res
                        queue.append((al, ac))
                        visitados.add((al, ac))
                res += 1

        for l in range (n):
            for c in range(n):
                if grid[l][c] == 1:
                    dfs(l, c)
                    return bfs()


exemplo1 = Solution()
print(f'Primeiro exemplo: {exemplo1.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])}')

exemplo2 = Solution()
print(f'O segundo caso de teste: {exemplo1.shortestBridge([[0,1,0],[0,0,0],[0,0,1]])}')