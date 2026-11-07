class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        #this qn can be done with dfs cycle detection but union find has a better complexity. we can do this in almost linear time
        parent = [i for i in range(len(edges)+1)]
        rank = [0]*(len(edges)+1)

        def findParent(a):
            if parent[a] != a:
                parent[a] = findParent(parent[a])
            return parent[a]

        def union(a, b):
            parentA = findParent(a)
            parentB = findParent(b)
            if parentA == parentB: #already connected
                return [a,b]
            
            if rank[parentA] > rank[parentB]:
                parent[parentB] = parentA
            elif rank[parentB] > rank[parentA]:
                parent[parentA] = parentB
            else:
                parent[parentA] = parentB
                rank[parentB] += 1

        for v, e in edges:
            if union(v,e):
                return union(v,e)