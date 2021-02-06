import pygame
pygame.init() #initialisation
window = pygame.display.set_mode((1200,400))
track = pygame.image.load('track5.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car,(30,60))
car_x = 150
car_y = 280
cam_x_offset = 0
cam_y_offest = 0
direction = 'up'
drive = True
focal_dis = 25#(30+10) for tracking the path
clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offest +15
    up_px = window.get_at((cam_x,cam_y - focal_dis))[0] #upwards negative y
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    #change direction -> right turn
    if direction== 'up' and up_px!=255 and right_px==255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car,-90)
    elif direction == 'right' and right_px!=255 and down_px==255:
        direction = 'down'
        car_x+=30
        cam_x_offset=0
        cam_y_offest=30
        car = pygame.transform.rotate(car,-90)
    elif direction=='down' and down_px!=255 and right_px:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offest = 0
        car = pygame.transform.rotate(car,90)
    elif direction=='right' and right_px!=255 and up_px:
        direction = 'up'
        car_x +=30
        cam_x_offset=0
        car = pygame.transform.rotate(car,90)
    #drive
    if(direction=='up' and up_px==255):
        car_y-=2
    elif(direction=='right' and right_px==255):
        car_x = car_x + 2
    elif(direction=='down' and down_px==255):
        car_y +=2
    # to display the track
    window.blit(track,(0,0))#block image transfer
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y),5,5)#centre,radius,thickness
    pygame.display.update()
