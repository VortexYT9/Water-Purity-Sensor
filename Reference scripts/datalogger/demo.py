import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('fivethirtyeight')

x_vals =[]
y_vals =[]


index = count()


def animate(i):
    data = pd.read_csv('data/cpu.csv')
    x = data['cpu']
    y = data['vmemory']

    plt.cla()

    plt.plot(x, y, label = 'Channel 1') 

    plt.legend(loc ='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()
plt.show()
