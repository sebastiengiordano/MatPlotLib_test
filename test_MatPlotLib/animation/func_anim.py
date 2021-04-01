import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(fileDir, "animation\\GBPUSD1d.txt")
    pullData = open(file_path,"r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    zar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y,z = eachLine.split(',')
            xar.append(int(x))
            yar.append(float(y))
            zar.append(float(z))
    ax1.clear()
    ax1.plot(xar,yar)
    ax1.plot(xar,zar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()