import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
import math
plt.grid()
pi=math.pi
h=60
theta1=pi/3
theta2=pi/4
x=math.tan(theta1)*h
y=math.tan(theta2)*h
answer=x+y
plt.annotate("Light house",[3,h-1])
plt.annotate("A",[x+1,1])
plt.annotate("B",[-y+3,1])
plt.annotate("60\N{DEGREE SIGN}",[2,h-7])
plt.annotate("45\N{DEGREE SIGN}",[-9,h-7])
plt.annotate("60m",[1,h/2])
plt.annotate("x",[x/2,1])
plt.annotate("y",[-y/2,1])
plt.plot([-y,x],[0,0],marker='o')
plt.plot([-y,0],[0,h],marker='o')
plt.plot([0,x],[h,0],marker='o')
plt.plot([0,0],[h,0],marker='o')
plt.show()
if(164==round(answer)):
    print("proved")