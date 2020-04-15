import pygame
import person
import city
import matplotlib.pyplot as plt

width=800
length=800

WHITE=[255,255,255]
BLACK=[0,0,0]

milan=city.city(N=100,simulation_timer=15000,show=True)

milan.run_simulation()
data=milan.results
plt.plot(data[0])
plt.plot(data[1])
plt.plot(data[2])
plt.legend(['fine','sick','healed'])
plt.xlabel('time')
plt.ylabel('number of individuals')
plt.show()