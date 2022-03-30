import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
import math
plt.grid()
pi=math.pi
a=math.tan(pi/3)
b=math.tan(pi/4)
c=(a+b)*60
plt.plot(a,b)
plt.annotate("Light house",[3,59])
plt.annotate("A",[60*a+1,1])
plt.annotate("B",[-60*b+3,1])
plt.annotate("60\N{DEGREE SIGN}",[2,53])
plt.annotate("45\N{DEGREE SIGN}",[-9,53])
plt.annotate("60m",[1,30])
plt.annotate("60"+b'\xfb'.decode('cp437')+"3m",[50,1])
plt.annotate("60m",[-50,1])
plt.plot([-60*b,60*a],[0,0],marker='o')
plt.plot([-60*b,0],[0,60],marker='o')
plt.plot([0,60*a],[60,0],marker='o')
plt.plot([0,0],[60,0],marker='o')
mp.Arc([0,0],1,1,angle=60,theta1=270)
plt.show()
if(164==round(c)):
    print("proved")