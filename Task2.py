import numpy as np
from scipy import ndimage

shape = input()
M = int(shape.split()[0])
matrix = []

for _ in range(M):
    row = input()
    matrix.append(np.fromstring(row, dtype=int, sep=' '))

map = np.array(matrix)

_, num_islands = ndimage.label(map)

print(num_islands)