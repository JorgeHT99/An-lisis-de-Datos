import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(1,10,0.1)
y1 = abs(x-5)
y2 = np.sin(x) 
y3 = 10 * x + 4* np.random.randn(1)
y4 = (25-(x-5)**2)**(1/2)+5
y5 = x**2
plt.figure(figsize=(7,7))

g1 = plt.subplot(3,3,(1,3))
g1.plot(x,y1,color = 'red', label = '$y=|x|$')
g1.legend()
g1.grid(True)

g2 = plt.subplot(3,3,(4,5))
g2.plot(x,y2,color = 'blue', label = '$y=sin(x)$')
g2.legend()
g2.grid(True)

g3 = plt.subplot(3,3,(6,9))
g3.plot(x,y3)
g3.grid(True)

g4 = plt.subplot(3,3,8)
g4.plot(x,y4,'--',color = 'yellow', label = '$y=|x|$')
g4.grid(True)
g2.legend()

g5 = plt.subplot(3,3,7)
g5.plot(x,y5,'-.',color ='green',label = '$y=x$')
g5.grid(True)
g2.legend()