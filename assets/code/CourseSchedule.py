class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        g = defaultdict(list)
        indeg = defaultdict(int)
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        q = deque(x for x in range(numCourses) if indeg[x] == 0)
        saw = 0
        while q:
            current = q.popleft()
            saw += 1
            for nei in g[current]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return saw == numCourses
