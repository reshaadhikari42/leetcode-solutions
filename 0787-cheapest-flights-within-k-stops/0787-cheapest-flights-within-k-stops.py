class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        '''
lets also try to solve this using modified dijkstra. we only take the nodes in the heap if their stops is less than k
because of this, we cannot use visit set. this will most likely cause a TLE but lets see what we can do
'''
        adj_list = defaultdict(list)
        best_stops = [float('inf')]*n
        for s,d,w in flights:
            adj_list[s].append((d,w))

        heap = [(0, src, 0)] #cost, src, stops
        while heap:
            weight, node, stops = heapq.heappop(heap)
            if node == dst:
                return weight

            if best_stops[node] < stops: #if we previously found a node with lesser stops(and lesser weight cause of heap) we just ignore this one
                continue

            best_stops[node] = stops
            if stops < k + 1: #we need k + 1 stops. we run until stops is less than k+1 bc we need to add one more.
                for d,w in adj_list[node]: #neighbors
                    heapq.heappush(heap, (w+weight, d, stops + 1))
        return -1

        '''
If you arrive with more or equal flights used than the note says: you’re pricier and have no more flights left. Strictly worse, so skip.
If you arrive with fewer flights used than the note says: you’re pricier, but you have more flights left, so you might get somewhere the earlier trip can’t. Keep going and update the note.

this means that it will ignore any node that was reached with more than k steps. why do we care about such a node anyway?
'''