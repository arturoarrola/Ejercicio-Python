     import sys, pygame
pygame.init()
tam_x=800
speed_x=0
tam_y=400
screen = pygame.display.set_mode([tam_x, tam_y])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        rec_1=pygame.draw.rect(screen, "White",(100,200,25,100))
        rec_2=pygame.draw.rect(screen, "White",(700,200,25,100))
        my_circle=pygame.draw.circle(screen, "white", (400,200),10)

 #cuando pongo esto el porgrama no se abre.
     if 100== tam_x - 50 or 100 == 0:
            speed_x *= -1
        if 100 == tam_y- 50 or 100 == 0:
            1 *= -1

        100 += speed_x 
        100 += 1
        #cuando pongo esto el porgrama no se abre.
