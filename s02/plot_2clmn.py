import numpy as np
import sys
import matplotlib.pylab as plt
file_name = sys.argv[1]
data = np.loadtxt(file_name)


# print(data)
# print(data.shape)


sh = data.shape
if sh[0]!=2:
    if sh[1]!=2:
        print('your data shape is not 2 column data! ')
        exit()

    x = data[:,0]
    y = data[:,1]

if sh[1] != 2:
    x = data[0,:]
    y = data[1,:]

plt.plot(x,y)
plt.savefig(sys.argv[1]+'.jpg',dpi=400)
plt.show()
