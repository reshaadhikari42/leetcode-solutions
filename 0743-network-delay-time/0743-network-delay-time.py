class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for v,e,w in times:
            adj_list[v].append([e,w])

        heap = []
        heapq.heappush(heap,[0,k]) #distance, source.
        visit = set()
        max_distance = 0

        while heap:
            distance, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            max_distance = distance #bc of heap property, we know that whatever dist we pop is the smallest distance to get to the node
            for nei, weight in adj_list[node]:
                heapq.heappush(heap, (distance+weight, nei))

        if len(visit) == n:
            return max_distance
        else:
            return -1