import numpy as np
import pygame
import person

width=1000
length=1000

WHITE=[255,255,255]
BLACK=[0,0,0]




class city():
    def __init__(self, N=100 ,simulation_timer=10000, show=True, allowed_to_move=0.1):
        self.N=N
        self.person_list=[person.person(movement=np.random.random()<allowed_to_move) for pg in range(self.N)]
        self.person_list[0].state='sick'
        self.results=np.array([self.N-1,1,0])
        self.simulation_time=simulation_timer
        self.show=show
        self.moving=allowed_to_move

    def run_simulation(self):

        time=0
        if self.show:
            pygame.init()
            screen = pygame.display.set_mode((width, length))
            screen.fill(WHITE)
        while time<self.simulation_time:

            self.possible_collision()
            for pg in self.person_list:
                pg.healing()
                if pg.can_move:
                    pg.movement()
                if self.show:
                    pg.draw(screen)
            if self.show:
                pygame.display.flip()
                screen.fill(WHITE)
            self.save_data()

            print(time/self.simulation_time*100)
            time+=1
        pygame.quit()

    def save_data(self):
        n_sick=0
        n_heal=0
        n_fine=0
        for pg in self.person_list:
            if pg.state=='sick':
                n_sick+=1
            elif pg.state=='heal':
                n_heal+=1
            elif pg.state=='fine':
                n_fine+=1
        result_time=np.array([n_fine,n_sick,n_heal])
        self.results=np.c_[self.results,result_time]

    def possible_collision(self):
        min_dist=(person.radius_ball * 2)**2
        for i in range(self.N):
            j=i+1
            while j<self.N:
                p1=self.person_list[i]
                p2=self.person_list[j]
                if (p1.x-p2.x)**2+(p1.y-p2.y)**2<min_dist:
                    person.collision(p1,p2)
                j+=1

