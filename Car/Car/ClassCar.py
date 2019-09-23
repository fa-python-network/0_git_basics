import pygame
pygame.init()

class Car(object):
    def __init__(self, surface):
        coords=[surface.get_width()//2, surface.get_height()//2]

        #Вверх
        self.car_surf_up=pygame.image.load('car.png').convert_alpha()
        self.car_rect_up=self.car_surf_up.get_rect(center=coords)
        #Вниз
        self.car_surf_down=pygame.transform.flip(self.car_surf_up, 0, 1)
        self.car_rect_down=self.car_surf_down.get_rect()
        #Вправо
        self.car_surf_right=pygame.transform.rotate(self.car_surf_up, 90)
        self.car_rect_right=self.car_surf_right.get_rect()
        #Влево
        self.car_surf_left=pygame.transform.flip(self.car_surf_right, 1, 0)
        self.car_rect_left=self.car_surf_left.get_rect()







