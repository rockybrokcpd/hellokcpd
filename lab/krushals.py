class Graph:
    def __init__(self, ver):
        self.V = ver
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def find(self, par, i):
        if par[i] == i:
            return i
        return self.find(par, par[i])
    def apply_union(self, par, rank, x, y):
        xr = self.find(par, x)
        yr = self.find(par, y)
        if rank[xr] < rank[yr]:
            par[xr] = yr
        elif rank[xr] > rank[yr]:
            par[yr] = xr
        else:
            par[yr] = xr
            rank[xr] += 1
    def kruskal_algo(self):
        res = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        par = []
        rank = []
        for node in range(self.V):
            par.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(par, u)
            y = self.find(par, v)
            if x != y:
                e = e + 1
                res.append([u, v, w])
                self.apply_union(par, rank, x, y)
        for u, v, weight in res:
            print("%d - %d: %d" % (u, v, weight))
g = Graph(5)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 7)
g.kruskal_algo()