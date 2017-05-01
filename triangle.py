import numpy as np
from math import floor

point=[(0.,0.),(1.,0.),(0.5,1.)]

start=[0.5,0.1]

for i in range(1000000):
        r=int(floor(3.*np.random.random()))
        start[0]=(start[0]+point[r][0])/2.
        start[1]=(start[1]+point[r][1])/2.
        print start[0],start[1]
