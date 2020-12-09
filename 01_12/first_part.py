import numpy as np
from itertools import combinations
data = np.loadtxt('input1')
for i in combinations(data,2):
    if sum(i) == 2020:
        print(i[0]*i[1])
        break
