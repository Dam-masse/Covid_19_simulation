import numpy as np

import matplotlib.pyplot as plt

import pygame

x_max=800
y_max=800

WHITE=[255,255,255]
BLACK=[0,0,0]
radius_ball=10

min_sick_time=5000

probability_of_contagious=0.1
probability_of_healing=0.001
def collision(p1,p2):
    tmp_array=p1.speed_array
    p1.speed_array=p2.speed_array
    p2.speed_array=tmp_array
    p2.movement()
    if (p1.state=='sick' or p2.state=='sick') and not (p1.state=='heal' or p2.state=='heal'):
        if np.random.random()<probability_of_contagious:
            p1.state='sick'
            p2.state='sick'


color_dic={'fine':[0,255,0],'sick':[255,0,0],'heal':[0,0,255],'death':[255,255,255]}


class person():

    def __init__(self):

        self.x=np.random.randint(0,x_max/10)*10
        self.y=np.random.randint(0,y_max/10)*10
        self.angle=2*np.pi*np.random.random()
        self.speed=1
        self.speed_array=np.array([self.speed*np.cos(self.angle),self.speed*np.sin(self.angle)])
        self.state='fine' # 'fine','sick','heal'
        self.sick_time=0

    def draw(self, screen):
        #drawing function screen is a surface in pygame
        pygame.draw.circle(screen,color_dic[self.state],(int(self.x), int(self.y)), radius_ball)
    
    def movement(self):
        # this will move the point
        # might be necessary to normalize speed and time

        new_x= self.x+self.speed_array[0]
        new_y= self.y+self.speed_array[1]
        if new_x>x_max or new_x<0:
            self.speed_array[0]=-self.speed_array[0]
        if new_y > y_max or new_y < 0:
            self.speed_array[1] = -self.speed_array[1]

        self.x=self.x+self.speed_array[0]
        self.y=self.y+self.speed_array[1]
        self.healing()

    def healing(self):
        if self.state=='sick':
            self.sick_time += 1
            if self.sick_time>min_sick_time:
                if np.random.random()<probability_of_healing:
                    self.state='heal'


