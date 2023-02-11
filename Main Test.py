from mst import Graph
import heapq
import numpy as np
import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances



x= Graph('data/large.csv')
x.construct_mst()
print(x.get_weights())
print(x.mst_mat)













