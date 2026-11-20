class Solution:
    '''
    apparently we have to use heirholzer's algorithm for eulerian path here
heirholzer's algo is similar to topological sort. 
it stores the nodes in opposite order. the difference is that since we wanna visit every edge once,
we gotta remove the edge after we use it.

also since we want it sorted, we will sort our adj_list[keys] in reverse so we can pop from back in O(1) time
'''
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj_list = {src:[] for src,dest in tickets}
        tickets = sorted(tickets, reverse = True)

        for src, dst in tickets:
            adj_list[src].append(dst)

        res = []
        def heirholzerDFS(src):
        #no base case bc while loop exits automatically when all edges are consumed
            while src in adj_list and adj_list[src]:
                nei = adj_list[src].pop() #smallest node at last so pop that
                heirholzerDFS(nei)

            res.append(src)

        heirholzerDFS('JFK')
        return res[::-1]

        #very fast. takes only O(ElogE) because of sorting. space is O(E) as each edge is visited only once.