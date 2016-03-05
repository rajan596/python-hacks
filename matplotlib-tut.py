# python 3

from matplotlib import pyplot as plt
from matplotlib import style

# styles
style.use('ggplot')
#style.use('dark_background')
#style.use('grayscale')

# points
x=[1,2,3,4]
y1=[2,5,6,7]
y2=[1,2,5,7]
y3=[1,2,3,4]

# chart/graph style
#plt.plot(x,y1,'b',linewidth=2,label='Y1')
#plt.scatter(x,y2,color='g',label='Y2')
#plt.plot(x,y3)
plt.bar(x,y1,color='c',align='center')

# settings
plt.title('Chart')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend()
#plt.grid(True,color='k')

# finally sow
plt.show()
