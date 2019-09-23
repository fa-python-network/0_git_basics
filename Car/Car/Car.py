import pygame
pygame.init()
from ClassCar import Car

white=(255, 255, 255)
sc=pygame.display.set_mode((2000, 1000))
sc.fill(white)
pygame.display.set_caption('Car')

car=Car(sc, 3)
sc.blit(car.car_surf_up, car.car_rect_up)
pygame.display.update()

flag=True
while flag:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            flag=False
        pressed=pygame.key.get_pressed()

    if pressed[pygame.K_UP] and not(pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT]):
        sc.fill(white)
        car.up()
        pygame.display.update()
    elif pressed[pygame.K_DOWN] and not(pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT]):
        sc.fill(white)
        car.down()
        pygame.display.update()
    elif pressed[pygame.K_RIGHT] and not(pressed[pygame.K_UP] or pressed[pygame.K_DOWN]):
        sc.fill(white)
        car.right()
        pygame.display.update()
    elif pressed[pygame.K_LEFT] and not(pressed[pygame.K_UP] or pressed[pygame.K_DOWN]):
        sc.fill(white)
        car.left()
        pygame.display.update()
    elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
        sc.fill(white)
        car.upright()
        pygame.display.update()
    elif pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
        sc.fill(white)
        car.upleft()
        pygame.display.update()
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
        sc.fill(white)
        car.downleft()
        pygame.display.update()
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
        sc.fill(white)
        car.downright()
        pygame.display.update()


    pygame.time.delay(15)