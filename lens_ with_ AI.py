import pygame, math
pygame.init()

# Setup
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()

# Lens center and object motion
X0, Y0 = 650, 450
Xs = 300
dx = 5

# Load images
lens = pygame.image.load('Lens and Axis2.png')

# Position images
lens_rect = lens.get_rect(center=(X0, Y0))


def source_position(speed_scale):
    global Xs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Xs -= dx * speed_scale
    if keys[pygame.K_RIGHT]:
        Xs += dx * speed_scale

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('gold')
    screen.blit(lens, lens_rect)    #pygame.draw.circle(screen, 'blue', (1040,447),5, width=0)    
    source_position(0.2)

    d1x = X0 - Xs
    if 449 < Xs < 450:
        Xs = 448
    elif 450 < Xs < 451:
        Xs = 452

    d1y = 100
    if d1x == 0:  # avoid division by zero
        continue

    # Lens formula: 1/f = 1/d1 + 1/d2
    d2x = 1 / (1 / 200 - 1 / d1x)
    d2y = d2x * d1y / d1x

    Ximage = X0 + d2x
    Yimage = Y0 + d2y

    # Draw object (arrow)
    pygame.draw.polygon(screen, 'brown', [(Xs, Y0 - d1y),(Xs - 10, Y0),
        (Xs + 10, Y0)])

    # Draw image (arrow)
    m = d2x / d1x  # magnification
    image_color = 'brown' if d1x > 200 else 'pink'
    pygame.draw.polygon(screen, image_color, [(X0 + d2x - 10 * m, Y0),
        (X0 + d2x + 10 * m, Y0),(Ximage, Yimage)])

    # Draw rays
    pygame.draw.line(screen, 'black', (Xs, Y0 - d1y), (X0, Y0 - d1y), 3)
    pygame.draw.line(screen, 'black', (X0, Y0 - d1y), (Ximage, Yimage), 3)
    pygame.draw.line(screen, 'black', (Xs, Y0 - d1y), (Ximage, Yimage), 3)

    pygame.display.update()
    clock.tick(60)
