import pygame,math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1300,900])

X0,Y0=650,450 #положение центра линзы на экране
lens=pygame.image.load('lens.png')
lens_rect=lens.get_rect(center=(X0,Y0))

axis=pygame.image.load('axis.png')
axis_rect=axis.get_rect(center=(X0,Y0))

X1,Y1=X0-200,Y0 #положение левого фокуса линзы на экране
foc1=pygame.image.load('circle.png')
foc1_rect=foc1.get_rect(center=(X1,Y1))

X11,Y11=X0-400,Y0 #положение двойного левого фокуса линзы на экране
foc2=pygame.image.load('circle.png')
foc2_rect=foc1.get_rect(center=(X11,Y11))

X2,Y2=X0+200,Y0 #положение правого фокуса линзы на экране
foc3=pygame.image.load('circle.png')
foc3_rect=foc1.get_rect(center=(X2,Y2))

X22,Y22=X0+400,Y0 #положение двойного правого фокуса линзы на экране
foc4=pygame.image.load('circle.png')
foc4_rect=foc1.get_rect(center=(X22,Y22))
Xs=300 #положения обьекта на экране
dx,dy=5,5
def source_position(a):
    global Xs,Ys
    button=pygame.key.get_pressed()
    if button[pygame.K_LEFT]:  Xs=Xs-dx*a
    if button[pygame.K_RIGHT]: Xs=Xs+dx*a
    
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill('gold')
    screen.blit(lens,lens_rect)
    screen.blit(axis,axis_rect)
    screen.blit(foc1,foc1_rect)
    screen.blit(foc2,foc2_rect)
    screen.blit(foc3,foc3_rect)
    screen.blit(foc4,foc4_rect)
    source_position(0.04)
    d1x=X0-Xs # величина сдвига обьекта относительно линзы по оси Х (слева от линзы)
    if Xs>449 and Xs<450:
        Xs=452
    if Xs<451 and Xs>450:
        Xs=448
    d1y=100 # высота обьекта
    d2x=1/(1/200-1/d1x) # величина сдвига изображения относительно линзы по оси Х (справа от линзы)
    d2y=d2x*d1y/d1x # высота изображения
    Ximage=X0+d2x # положение  изображенияпо оси Х
    Yimage=Y0+d2y  # положение изображения по оси Y
    P_image1=(Ximage,Y0) # положение верхней точки изображения на экране(координатной оси)
    P_image2=(Ximage,Yimage) # положение нижней точки изображения на экране(координатной оси)  
    m=d2x/d1x  #коэффициент увеличения
    P1=(Xs,Y0-d1y)
    P2=(Xs-10,Y0)
    P3=(Xs+10,Y0)
    pygame.draw.polygon(screen,'brown',(P1,P2,P3))
    P11=(X0+(d2x-10*m),Y0)
    P21=(X0+(d2x+10*m),Y0)
    P31=P_image2
    if d1x>200:
        pygame.draw.polygon(screen,'brown',(P11,P21,P31))
    if d1x<=200:
        pygame.draw.polygon(screen,'pink',(P11,P21,P31))
    Point1=(Xs,Y0-d1y)# Point1=P1
    Point2=(X0,Y0-d1y)
    pygame.draw.line(screen,'black',Point1,Point2,3)
    pygame.draw.line(screen,'black',Point2,P_image2,3)
    Point3=P_image2
    pygame.draw.lines(screen,'black',True,[Point1,Point3],3)
    pygame.display.update()
    clock.tick(400)
    
