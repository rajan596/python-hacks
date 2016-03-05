# python3
# chart from csv file

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y=np.loadtxt('graphdata.csv',
                unpack=True,
                delimiter=','
               )

plt.plot(x,y)

plt.title('chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
