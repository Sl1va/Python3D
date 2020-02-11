import pygame

from vector import Vector, Point

pygame.init()
screen = pygame.display.set_mode((1024, 840))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


running = True
mouse_pressed = False

camera = Vector(0, 1, 0)

prev_pressed = [0, 0]

A = Point(0, 0, 0)
B = Point(200, 0, 0)
C = Point(200, 200, 0)
D = Point(0, 200, 0)
A1 = Point(0, 0, 200)
B1 = Point(200, 0, 200)
C1 = Point(200, 200, 200)
D1 = Point(0, 200, 200)


while running:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

    cur_pressed = pygame.mouse.get_pos()
    if mouse_pressed:
        camera.x -= (cur_pressed[0] - prev_pressed[0]) / 400
        camera.y -= (cur_pressed[1] - prev_pressed[1]) / 400
        # поделить на 400, чтобы более-менее плавно вращать

    A_ = A.get2D(camera)
    B_ = B.get2D(camera)
    C_ = C.get2D(camera)
    D_ = D.get2D(camera)
    A1_ = A1.get2D(camera)
    B1_ = B1.get2D(camera)
    C1_ = C1.get2D(camera)
    D1_ = D1.get2D(camera)

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, A_, A1_)
    pygame.draw.line(screen, BLACK, A_, B_)
    pygame.draw.line(screen, BLACK, A_, D_)

    pygame.draw.line(screen, BLACK, B_, C_)
    pygame.draw.line(screen, BLACK, B_, B1_)

    pygame.draw.line(screen, BLACK, C_, C1_)
    pygame.draw.line(screen, BLACK, C_, D_)

    pygame.draw.line(screen, BLACK, D_, D1_)

    pygame.draw.line(screen, BLACK, A1_, B1_)
    pygame.draw.line(screen, BLACK, A1_, D1_)

    pygame.draw.line(screen, BLACK, D1_, C1_)
    pygame.draw.line(screen, BLACK, B1_, C1_)

    pygame.display.flip()

    prev_pressed = cur_pressed

pygame.quit()
