import numpy as np
from . import tools

# reference : https://arxiv.org/abs/1604.02808
# edge format: (origin, neighbor)

num_node = 15
self_link = [(i, i) for i in range(num_node)]
inward_ori_index = [(1,2),(2,3),(2,4),(3,5),(5,6),(4,13),(13,14),
                              (2,15),(15,7),(7,8),(8,9),(15,12),(12,10),(10,11)]
inward = [(i - 1, j - 1) for (i, j) in inward_ori_index]
outward = [(j, i) for (i, j) in inward]

neighbor = inward + outward


class Graph():
    """ The Graph to model the skeletons in NTU RGB+D

    Arguments:
        labeling_mode: must be one of the follow candidates
            uniform: Uniform Labeling
            dastance*: Distance Partitioning*
            dastance: Distance Partitioning
            spatial: Spatial Configuration
            DAD: normalized graph adjacency matrix
            DLD: normalized graph laplacian matrix

    For more information, please refer to the section 'Partition Strategies' in our paper.

    """

    def __init__(self, labeling_mode='uniform'):
        self.A = self.get_adjacency_matrix(labeling_mode)
        self.num_node = num_node
        self.self_link = self_link
        self.inward = inward
        self.outward = outward
        self.neighbor = neighbor

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'uniform':
            A = tools.get_uniform_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'distance*':
            A = tools.get_uniform_distance_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'distance':
            A = tools.get_distance_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'spatial':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)
        elif labeling_mode == 'DAD':
            A = tools.get_DAD_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'DLD':
            A = tools.get_DLD_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'FC':
            A= np.ones((num_node, num_node))

        # elif labeling_mode == 'customer_mode':
        #     pass
        else:
            raise ValueError()

        print(A)
        return A


def main():
    mode = ['uniform', 'distance*', 'distance', 'spatial', 'DAD', 'DLD']
    np.set_printoptions(threshold=np.nan)
    for m in mode:
        print('=' * 10 + m + '=' * 10)
        print(Graph(m).get_adjacency_matrix())


if __name__ == '__main__':
    main()
