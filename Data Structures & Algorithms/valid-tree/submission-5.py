class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)
        
        for u, v in edges:
            if u == v:
                return False
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True

        if not dfs(0, 0):
            return False
        return len(visited) == n