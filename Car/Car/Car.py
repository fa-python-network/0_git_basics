import pygame
pygame.init()
from ClassCar import Car

white=(255, 255, 255)
sc=pygame.display.set_mode((2000, 1000))
sc.fill(white)
pygame.display.set_caption('Car')

car=Car(sc)
sc.blit(car.car_surf_up, car.car_rect_up)
pygame.display.update()

flag=True
while flag:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            flag=False


    pygame.time.delay(20)