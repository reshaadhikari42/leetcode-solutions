class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for v,e,w in times:
            adj_list[v].append([e,w])

        heap = []
        heapq.heappush(heap, (0, k))#weight and node. node here is k i.e source node
        visit = set()
        distance = [float('inf')]* (n+1) #except source node tho
        distance[k] = 0
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            for nei,weight in adj_list[node]:
                new_dist = dist+weight
                if new_dist < distance[nei]:
                    distance[nei] = new_dist
                    heapq.heappush(heap,(new_dist, nei))

        if float('inf') in distance[1:]:
            return -1

        return max(distance[1:])