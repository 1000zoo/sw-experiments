"""
    practice #2
    함수로 그래프 그리기
    - 입력 데이터 (x) 는 -5 부터 5 까지 0.1 간격으로 선언
    - 4개의 함수를 하나의 figure 창에 그리기
      (y = 2x + 1, y = -x^2 + 2, y = sinx, y = cosx)
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)
y1 = 2 * x + 1
y2 = -x ** 2 + 2         # 파이썬의 ** 연산은 부호연산자인 - 보다 우선시된다.
y3 = np.sin(x)
y4 = np.cos(x)

plt.subplot(2,2,1)
plt.plot(x, y1)
plt.title("y = 2x + 1")
plt.subplot(2,2,2)
plt.plot(x, y2)
plt.title("y = -x^2 + 1")
plt.subplot(2,2,3)
plt.plot(x, y3)
plt.title("y = sin(x)")
plt.subplot(2,2,4)
plt.plot(x, y4)
plt.title("y = cos(x)")
plt.show()