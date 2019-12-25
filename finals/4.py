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

    def shortest_path(self, s, e, visited=[], path=([], math.inf), dist=0):
        visited = visited + [s]

        if s == e:
            print(visited, dist)
            if dist < path[1]:
                return visited, dist
            return path
        
        # neighbors of current node 
        neighbors = [x for x in self.E if x[0] == s]
        for i in list(neighbors):
            if i[1] not in visited:
                path = self.shortest_path(i[1], e, visited, path, dist + i[2])
        
        return path 

    def edge_brute_force(self, V, E, generated = [], save = []):
        if len(generated) == 2:
            return save + [generated]

        for i in V:
            V_copy = V.copy()
            V_copy.remove(i)
            save = self.edge_brute_force(V_copy, E, generated + [i], save)
        
        return save

    def mst_prim(self, E):
        E = E.copy()

        mst_tree = []

        min_node = min(E, key=lambda t: t[2])

        while(len(E) != 0):
            mst_tree += [min_node]

            # remove nodes from Edges
            E.remove(min_node)
            E.remove((min_node[1], min_node[0], min_node[2]))

            neighbors = [x for x in E if x[0] == min_node[0] or x[0] == min_node[1]]

            if len(neighbors) != 0:
                min_node = min(neighbors, key=lambda t: t[2])
                neighbors.remove(min_node)
                check_neighbors = [x for x in E if x[0] == min_node[0] or x[0] == min_node[1]]
                

                for i in neighbors:
                    if i not in check_neighbors:
                        E.remove(i)
                        E.remove((i[1], i[0], i[2]))

            # print(neighbors)
        
        return mst_tree, sum(x for _, _, x in mst_tree)
    
    def added_mst(self):
        all_edges = self.edge_brute_force(self.V, self.E)
        current_edges = [[x, y] for x, y, _ in self.E]
        # print(current_edges)
        not_connected_edges = []
        for i in all_edges:
            if i not in current_edges and [i[1], i[0]] not in not_connected_edges:
                not_connected_edges += [i]
                
        # print(not_connected_edges)

        min = ([], math.inf)
        for i in not_connected_edges:
            temp = self.mst_prim(self.E + [(i[0], i[1], 1), (i[1], i[0], 1)])
            if temp[1] < min[1]:
                min = temp

        return min 
    
    def mst_prim_max(self, E):
        E = E.copy()

        mst_tree = []

        max_node = max(E, key=lambda t: t[2])

        while(len(E) != 0):
            mst_tree += [max_node]

            # remove nodes from Edges
            E.remove(max_node)
            E.remove((max_node[1], max_node[0], max_node[2]))

            neighbors = [x for x in E if x[0] == max_node[0] or x[0] == max_node[1]]
            print('neighbors: ', neighbors, 'max_node: ', max_node)

            if len(neighbors) != 0:
                max_node = max(neighbors, key=lambda t: t[2])
                neighbors.remove(max_node)
                check_neighbors = [x for x in E if x[0] == max_node[0] or x[0] == max_node[1]]
                

                for i in neighbors:
                    if i not in check_neighbors:
                        E.remove(i)
                        E.remove((i[1], i[0], i[2]))

            
        
        return mst_tree, sum(x for _, _, x in mst_tree)




#%%

g1 = G([1, 2, 3, 4, 5], [(1, 2, 10), (1, 4, 7), (2, 3, 18), (3, 5, 1), (4, 5, 2), (2, 4, 9), (1, 3, 9)])
# g1.shortest_path(1, 5)
# g1.mst_prim()
g2 = G([1, 2, 3, 4, 5, 6, 7], [(1, 2, 28), (2, 3, 16), (2, 7, 14), (3, 4, 12), (4, 5, 22), (4, 7, 18), (5, 6, 25), (5, 7, 24), (6, 1, 10)])

g1.added_mst()
g2.mst_prim_min(g2.E)
# %%


# %%
