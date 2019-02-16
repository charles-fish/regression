import pygame, math
import numpy as np
pygame.init()

H = 900
W = 2*H

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("regression")
plt = pygame.Surface((W,H))
plt.fill((0,0,0))

pi = math.pi

delay = 0

def nrm(x,m,s,a):
    v = 2*(s**2)
    w = a/(pi*v)**0.5
    return(w*math.exp(-(1/v)*(x-m)**2))

M = [0]*H
S = [0]*H
A = [0]*H

for i in range(H):
    y = i/H
    y2 = y**2
    y3 = y**3
    m = (y3 + 1)/4
    s = (y2 + 1)/20
    a = 1 + 196*y - 196*y2
    M[i] = m
    S[i] = s
    A[i] = a
    a = int(a)
    r = np.random.normal(m,s,a)
    for j in range(a):
        plt.set_at((int(r[j]*H),H-1-i),(125 + 50*(1-y),75 + 150*r[j]*y,150 + 10*r[j]))

t = -1

run = True
while run:
    t += 1
    t %= H
    pygame.time.delay(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    screen.blit(plt, (0,0))
    
    pygame.draw.line(screen, (150,150,150), (0,H-1-t), (H-1,H-1-t))

    for i in range(H):
        y = nrm(i/H,M[t],S[t],A[t])
        pygame.draw.aaline(screen, (125 + int(50*(1-t/H)),75 + int(150*i*t/(H*H)),150 + int(10*(i/H))), (H+i,int(H/2) + 4 - y), (H+i,int(H/2) - 4 - y),0)

    pygame.display.update()
