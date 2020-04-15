import numpy as np
import pygame
import person

width=800
length=800

WHITE=[255,255,255]
BLACK=[0,0,0]




class city():
    def __init__(self, N=100 ):
        self.N=N
        self.person_list=[person.person() for pg in range(self.N)]
        self.person_list[0].state='sick'
    def run_simulation(self):
        pygame.init()
        screen = pygame.display.set_mode((width, length))
        screen.fill(WHITE)
        while True:
            screen.fill(WHITE)
            self.possible_collision()
            for pg in self.person_list:
                pg.movement()

                pg.draw(screen)
            pygame.display.flip()
        pygame.quit()

    def possible_collision(self):
        for i in range(self.N):
            j=i+1
            while j<self.N:
                p1=self.person_list[i]
                p2=self.person_list[j]
                if np.abs(p1.x-p2.x)<person.radius_ball*2 and np.abs(p1.y-p2.y)<person.radius_ball*2:
                    person.collision(p1,p2)
                j+=1

