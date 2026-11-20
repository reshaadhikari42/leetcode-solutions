class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj_list = {src:[] for src,dst in tickets}
        tickets = sorted(tickets, reverse = True)
        for src, dst in tickets:
            adj_list[src].append(dst)

        res = []
        #heirholzer's algo
        def heirholzerDFS(src):
            while src in adj_list and len(adj_list[src]) > 0:
                nei = adj_list[src].pop()
                heirholzerDFS(nei)
            res.append(src)

        heirholzerDFS('JFK')
        return res[::-1]
            
        