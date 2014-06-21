import numpy as np
import matplotlib.pyplot as plt
from random import uniform



times = 100  # 試行回数
p = [[1,-1], [-1, 1], [-1,1], [1, -1]] #利得


x0 = [uniform(0, 1)] #初期信念をランダムに設定,appendを使い後に更新する
x1 = [uniform(0, 1)]


for t in range(times):
   ep0 = [p[0][0]*(1-x0[t])+p[1][0]*x0[t], p[2][0]*(1-x0[t])+p[3][0]*x0[t]]#期待利得
   ep1 = [p[0][1]*(1-x1[t])+p[2][1]*x1[t], p[1][1]*(1-x1[t])+p[3][1]*x1[t]]
   if ep0[0] > ep0[1]:
        a0 = 0
   else:
        a0 = 1
    
   if ep1[0] > ep1[1]:
        a1 = 0
   else:
        a1 = 1
   x0.append(x0[t]+(a1-x0[t])/(t+2))
   x1.append(x1[t]+(a0-x1[t])/(t+2))

plt.plot(x0, 'r-', label = 'x0(t)')
plt.plot(x1, 'b-', label = 'x1(t)')
plt.show()