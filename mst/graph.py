import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        start_v = self.adj_mat[0]   #initialize list of edges of first node
        num_vertices = len(start_v)
        mst = [[0] * num_vertices for i in range(num_vertices)] #initialize empty mst matrix to fill
        visited = [0]   #initialize list of nodes visited
        heap = list(start_v)   #initialize the heap
        heapq.heapify(heap)
        while len(visited) < num_vertices:  #runs the loop until all of the nodes are in visited
            curr_edge = heapq.heappop(heap)
            if curr_edge != 0:  #check that an edge exists
                for node in visited:    #Iterate through the edges of nodes visited to find the where the curr_edge is
                    edges = list(self.adj_mat[node])
                    if curr_edge in edges:
                        curr_node = node
                        add_node = edges.index(curr_edge)
                        if add_node not in visited: #If the node is new, add it to visited and add it's edges to the heap
                            visited.append(add_node)
                            heap += list(self.adj_mat[add_node])
                            heapq.heapify(heap)
                            mst[curr_node][add_node] = curr_edge
                            mst[add_node][curr_node] = curr_edge
                            break
        self.mst_mat = np.array(mst)

    def get_weights(self):
        depth = 1
        weight = 0
        for edges in self.mst_mat:
            for i in range(depth):
                weight += edges[i]
            depth += 1
        return weight





