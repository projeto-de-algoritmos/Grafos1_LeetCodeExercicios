from collections import deque, defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        for word in wordList:
            for chr in range(len(word)):
                diff = word[:chr] + "#" + word[chr + 1:]
                nei[diff].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        return self.BFS(q, visited, res, nei, endWord)
    
        
    def BFS(self, q, visited, res, nei, endWord):
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    diff = word[:j] + "#" + word[j+1:]
                    for neiWord in nei[diff]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1
        
        return 0
