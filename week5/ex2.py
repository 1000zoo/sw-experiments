"""
    ex2)
    data = np.zeros((3,3)) 일 때,
    1) 1차원으로 바꾸세요.
    2) index가 1,3,5,7에 값을 1로 바꾸세요.
    3) 다시 3x3 차원으로 바꾸세요.
"""

import numpy as np

data = np.zeros((3,3))
print(data)

#   1)
data_list = data.reshape((3*3, ))
print(data_list)
#   2)
for i in range(9):
    if i % 2 == 1:
        data_list[i] = 1
print(data_list)
#   3)
data_matrix = data_list.reshape((3, 3))
print(data_matrix)