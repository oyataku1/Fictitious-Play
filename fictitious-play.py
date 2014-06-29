import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from random import uniform

p = [[1,-1], [-1, 1], [-1,1], [1, -1]] #利得


        
def Fictplay(n):
    x0 = [uniform(0, 1)] #初期信念をランダムに設定,appendを使い後に更新する
    x1 = [uniform(0, 1)]
    
    for t in range(n):
            
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
            # append
        x0.append(x0[t]+(a1-x0[t])/(t+2))
        x1.append(x1[t] +(a0-x1[t])/(t+2))
    return x0, x1

x0, x1 = Fictplay(100)

            

#plt.plot(x0, 'r-', label = 'x0(t)')
#plt.plot(x1, 'b-', label = 'x1(t)')
#plt.savefig('fictplay.png')
#plt.show()

x0_last = []
for i in range(100):
    x0, x1 = Fictplay(10000)
    x0_last.append(x0[9999])
plt.hist(x0_last)
#plt.savefig('fictplay_hist.png')
plt.show()