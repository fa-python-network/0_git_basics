import pygame
pygame.init()

white=(255, 255, 255)
sc=pygame.display.set_mode((2000, 1000))
sc.fill(white)
pygame.display.set_caption('Car')


pygame.display.update()

flag=True
while flag:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            flag=False


    pygame.time.delay(20)