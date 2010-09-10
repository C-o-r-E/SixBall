import sys
import pygame
from pygame.locals import *
from musume import *

img_bg = "bgbig.png"
img_globe = "circle.png"
#img_rin = "Chibi_Rin.png"
#img_raven = "Raven.png"

pygame.init()
pygame.display.set_caption("6 ball")
screen = pygame.display.set_mode((640, 360))
pygame.key.set_repeat(5, 50)
sakuya = pygame.time.Clock()

font = pygame.font.Font(None, 17)

bg0 = pygame.image.load(img_bg).convert()
globe = pygame.image.load(img_globe).convert_alpha()
#cat = pygame.image.load(img_rin).convert_alpha()
#okuu = pygame.image.load(img_raven).convert_alpha()

maidens = []
cat = Orin("rin.png", (288, 25))
raven = Okuu("Raven.png", (0,0))

maidens.append(cat)
maidens.append(raven)

rot_theta = 0;

globe_image = globe.copy()
globe_center = (221, 81)
globe_pos = (221, 81)

bgclip = pygame.Rect(32, 172, 640, 630)
bg_image = bg0.copy()

final_bg = screen.copy()
bg_image.blit(final_bg, (0,0), bgclip)

#cat_image = cat.copy()
#okuu_image = okuu.copy()

updateRects = []

screen.blit(bg_image, (0, 0), bgclip)
screen.blit(globe_image, globe_pos)
pygame.display.flip()

msec = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            if event.key == K_LEFT:
                rot_theta -= 6
                globe_image = pygame.transform.rotate(globe, rot_theta)
                globe_pos = (globe_center[0]  - (globe_image.get_width() - globe.get_width())/2,
                             globe_center[1] - (globe_image.get_height() - globe.get_height())/2)

                bg_image = pygame.transform.rotate(bg0, rot_theta)
                bgclip = pygame.Rect(
                    32 + (bg_image.get_width() - bg0.get_width())/2,
                    172 + (bg_image.get_height() - bg0.get_height())/2,
                    640, 360)
                updateRects.append(screen.blit(bg_image, (0, 0), bgclip))
                updateRects.append(screen.blit(globe_image, globe_pos))
                final_bg.blit(bg_image, (0, 0), bgclip)
            if event.key == K_RIGHT:
                rot_theta += 6
                globe_image = pygame.transform.rotate(globe, rot_theta)
                globe_pos = (globe_center[0]  - (globe_image.get_width() - globe.get_width())/2,
                             globe_center[1] - (globe_image.get_height() - globe.get_height())/2)

                bg_image = pygame.transform.rotate(bg0, rot_theta)
                bgclip = pygame.Rect(
                    32 + (bg_image.get_width() - bg0.get_width())/2,
                    172 + (bg_image.get_height() - bg0.get_height())/2,
                    640, 360)
                updateRects.append(screen.blit(bg_image, (0, 0), bgclip))
                updateRects.append(screen.blit(globe_image, globe_pos))
                final_bg.blit(bg_image, (0, 0), bgclip)

            if event.key == K_DOWN and cat.rect.bottom < 86:
                cat.rect.centery += 6
                screen.blit(final_bg, cat.rect)
                updateRects.append(screen.blit(cat.image, cat.rect))
            if event.key == K_UP:
                cat.rect.centery -= 6
                screen.blit(final_bg, cat.rect)
                updateRects.append(screen.blit(cat.image, cat.rect))
                
    text = font.render(str(1000/msec) + "fps", True, (255, 255, 255))
    #screen.blit(bg_image, (0, 0), bgclip)
    #screen.blit(globe_image, globe_pos)
    #screen.blit(cat_image, (288, 25))
    #screen.blit(okuu_image, (0,0))
    
    updateRects.append(screen.blit(text, (640 - text.get_width(), 360 - text.get_height())))
    msec = sakuya.tick(60)
    pygame.display.update(updateRects)
    updateRects = []
    
