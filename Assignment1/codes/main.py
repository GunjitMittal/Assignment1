import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
import math
plt.grid()
pi=math.pi
h=60
theta1=pi/3
theta2=pi/4
a=math.tan(theta1)
b=math.tan(theta2)
c=(a+b)*h
plt.plot(a,b)
plt.annotate("Light house",[3,h-1])
plt.annotate("A",[h*a+1,1])
plt.annotate("B",[-h*b+3,1])
plt.annotate("60\N{DEGREE SIGN}",[2,h-7])
plt.annotate("45\N{DEGREE SIGN}",[-9,h-7])
plt.annotate("60m",[1,h/2])
plt.annotate("60"+b'\xfb'.decode('cp437')+"3m",[h*a/2,1])
plt.annotate("60m",[-h*b/2,1])
plt.plot([-h*b,h*a],[0,0],marker='o')
plt.plot([-h*b,0],[0,h],marker='o')
plt.plot([0,h*a],[h,0],marker='o')
plt.plot([0,0],[h,0],marker='o')
plt.show()
if(164==round(c)):
    print("proved")