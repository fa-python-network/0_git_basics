import pygame
pygame.init()

class Car(object):
    def __init__(self, surface, speed):
        self.coords=[surface.get_width()//2, surface.get_height()//2]
        self.surf=surface
        self.speed=speed
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
        #Вправо Вверх
        self.car_surf_upright=pygame.transform.rotate(self.car_surf_right, 45)
        self.car_rect_upright=self.car_surf_upright.get_rect()
        #Вправо Вниз
        self.car_surf_downright=pygame.transform.rotate(self.car_surf_down, 45)
        self.car_rect_downright=self.car_surf_downright.get_rect()
        #Влево Вниз
        self.car_surf_downleft=pygame.transform.rotate(self.car_surf_left, 45)
        self.car_rect_downleft=self.car_surf_downleft.get_rect()
        #Влево Вверх
        self.car_surf_upleft=pygame.transform.rotate(self.car_surf_up, 45)
        self.car_rect_upleft=self.car_surf_upleft.get_rect()


    def up(self):
        self.coords[1]-=self.speed+2**0.5
        self.car_rect_up.center=coords
        self.surf.blit(self.car_surf_up, self.car_rect_up)

    def down(self):
        self.coords[1]+=self.speed+2**0.5
        self.car_rect_down.center=coords
        self.surf.blit(self.car_surf_down, self.car_rect_down)

    def right(self):
        self.coords[0]+=self.speed+2**0.5
        self.car_rect_right.center=coords
        self.surf.blit(self.car_surf_right, self.car_rect_right)

    def left(self):
        self.coords[0]-=self.speed+2**0.5
        self.car_rect_left.center=coords
        self.surf.blit(self.car_surf_left, self.car_rect_left)

    def upleft(self):
        self.coords[0]-=self.speed
        self.coords[1]-=self.speed
        self.car_rect_upleft.center=coords
        self.surf.blit(self.car_surf_upleft, self.car_rect_upleft)

    def upright(self):
        self.coords[0]+=self.speed
        self.coords[1]-=self.speed
        self.car_rect_upright.center=coords
        self.surf.blit(self.car_surf_upright, self.car_rect_upright)

    def downright(self):
        self.coords[0]+=self.speed
        self.coords[1]+=self.speed
        self.car_rect_downright.center=coords
        self.surf.blit(self.car_surf_downright, self.car_rect_downright)

    def downleft(self):
        self.coords[0]-=self.speed
        self.coords[1]+=self.speed
        self.car_rect_downleft.center=coords
        self.surf.blit(self.car_surf_downleft, self.car_rect_downleft)






        










