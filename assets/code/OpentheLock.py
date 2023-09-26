from collections import deque

class Solution():

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def is_deadend(comb):
            return comb in deadends
        
        def get_neighbors(comb):
            neighbors = []
            for i in range(4):
                for j in [-1, 1]:
                    new_wheel_value = (int(comb[i]) + j) % 10
                    new_comb = comb[:i] + str(new_wheel_value) + comb[i+1:]
                    neighbors.append(new_comb)
            return neighbors

        visited = set()
        queue = deque(['0000'])
        visited.add('0000')
        level = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return level

                if is_deadend(current):
                    continue

                neighbors = get_neighbors(current)

                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            level += 1

        return -1
