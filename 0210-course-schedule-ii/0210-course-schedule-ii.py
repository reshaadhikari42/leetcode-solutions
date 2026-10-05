class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        '''
        same as course schedule but now we need order as well
        we use topological sort (stack) to return the answer-> stack[::-1]
        if we find a cycle, we return [] asap
        topological sort sorts in order of u,v where u-> v in graph
        '''
        #still need two sets to detect a cycle
        visiting, visited = set(), set()
        adj_list = defaultdict(list)
        stack = []
        for v,e in prerequisites:
            adj_list[e].append(v)

        def dfs(vertex):
            if vertex in visited:  #always check visited before visiting. because v in visited is also gonna be in visiting as we don't backtrack here
                return True
            if vertex in visiting:
                return False
            visiting.add(vertex)
            for nei in adj_list[vertex]:
                if dfs(nei) == False:
                    return False
            visited.add(vertex)
            stack.append(vertex)
            return True

        for v in range(numCourses):
            if dfs(v) == False:
                return []
        return stack[::-1]
        
        #time and space is O(V+E)