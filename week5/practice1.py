"""
    practice #1
    N 값을 입력 받아 N by N 행렬 만들기.
    값은 1 부터 시작하여 순차적으로 들어가게 하기
    ex)
    N = 5
    1 2 3 4 5
    6 7 8 ...
    .......25
"""

import numpy as np

n = int(input("N => "))

ndarray_list = np.arange(1, n * n + 1, 1.0).reshape((n, n))
print(ndarray_list)

