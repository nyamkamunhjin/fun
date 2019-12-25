# G = (V, E)
# V = [vertex1, vertex2, vertex3, ...]
# E = [(vertex1, vertex2, weight), (vertexN, vertexM, weight), ...]
#%%
import math
class G:
    def __init__(self, V, E, is_undirected=True):
        self.V = V
        self.E = E

        if is_undirected:
            for i in list(E):
                self.E = self.E + [(i[1], i[0], i[2])]

    def edge_brute_force(self, V, generated = [], save = []):
        if len(generated) == 2:
            return save + [generated]

        for i in V:
            V_copy = V.copy()
            V_copy.remove(i)
            save = self.edge_brute_force(V_copy, generated + [i], save)
        
        return save


    def shortest_path(self, s, e, visited=[], path=([], math.inf), dist=0):
        visited = visited + [s]

        if s == e:
            # print(visited, dist)
            if dist < path[1]:
                return visited, dist
            return path
        
        # neighbors of current node 
        neighbors = [x for x in self.E if x[0] == s]
        for i in list(neighbors):
            if i[1] not in visited:
                path = self.shortest_path(i[1], e, visited, path, dist + i[2])
        
        return path 

    def longest_path(self, s, e, visited=[], path=([], -math.inf), dist=0):
        visited = visited + [s]

        if s == e:
            print(visited, dist)
            if dist > path[1]:
                return visited, dist
            return path
        
        # neighbors of current node 
        neighbors = [x for x in self.E if x[0] == s]
        for i in list(neighbors):
            if i[1] not in visited:
                path = self.longest_path(i[1], e, visited, path, dist + i[2])
        
        return path 
    
    def max_diameter(self, s, e):
        return len(self.longest_path(s, e)[0]) - 2

    def max_shortest_path(self):
        shortest_paths = []
        all_edges = self.edge_brute_force(self.V)
        for i in all_edges:
            shortest_paths.append(self.shortest_path(i[0], i[1]))
        
        shortest_paths.sort(key =lambda t: t[1], reverse=True)
        return shortest_paths[0], shortest_paths[2]


#%%

g1 = G([1, 2, 3, 4, 5], [(1, 2, 10), (1, 4, 7), (2, 3, 18), (3, 5, 1), (4, 5, 2), (2, 4, 9), (1, 3, 9)])
g1.shortest_path(1, 5)

g1.longest_path(1, 5)


# %%
