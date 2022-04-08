"""
    ex1)
    1) arange 를 이용하여 data를 선언하세요.
    2) 1차원 배열을 2차원 (2x5) 으로 바꾸세요.
    3) 2차원으로 바뀐 배열을 Transpose 시키세요
    4) Transpose 된 배열을 axis=2 기준으로 합을 구하세요.
"""

import numpy as np

#   1)
data = np.arange(1, 11)
print(data)
#   2)
data_matrix = data.reshape((2, 5))
print(data_matrix)
#   3)
data_T = data_matrix.T      #  or data_T = data.transpose()
print(data_T)
#   4)
data_sum_axis2 = data_T.sum(axis=1)
print(data_sum_axis2)