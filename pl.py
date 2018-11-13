import matplotlib as mpl
import matplotlib.pyplot as plt
import math


def graph(stat):
    mpl.rcParams.update({'font.size': 10})
    plt.axis([0, 60, 0, 20])
    plt.title('People counter')
    plt.xlabel('Time, sec')
    plt.ylabel('People')
    x = []
    y = []

    for key in stat:
        x.append(key)
        y.append(stat[key])

    plt.plot(x, y, color='blue', linestyle='solid', label='f(x)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
