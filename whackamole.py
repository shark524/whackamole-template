import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        molepos = (0,0)
        molgrid = (0,0)
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    row = y//32
                    col = x//32
                    if (col, row) == molgrid:
                        newCol = random.randrange(0, 608)//32
                        newRow = random.randrange(0, 480)//32
                        molgrid = (newCol, newRow)
                        molepos = (newCol*32, newRow*32)
            screen.fill("light green")
            for i in range(1, 16):
                pygame.draw.line(screen, 'black', (0, i * 32), (640, i * 32), 1)
            for i in range(1, 20):
                pygame.draw.line(screen, 'black', (i * 32, 0), (i * 32, 512), 1)
            screen.blit(mole_image, mole_image.get_rect(topleft = molepos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
