import numpy as np
import matplotlib.pyplot as plt
import pygame as pg


x=np.linspace(0,2*np.pi,400)
y=np.sin(x)

plt.plot(x,y)
plt.show()