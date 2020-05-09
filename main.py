import pygame
import sys
import tile
import math
import grid
import menu

pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

screen.blit(background, (0, 0))
pygame.display.flip()
pygame.display.set_caption('Testy time!')
clock = pygame.time.Clock()

holdingTile = False
heldTile = tile.Tile(0, 0, 0)
tileGrid = grid.Grid((15, 15), (7, 11), 40)
itemMenu = menu.Menu((15, 350), (100, 100))

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if not holdingTile:
                if itemMenu.isInMenu(pos):
                    heldTile = itemMenu.getItem(pos)
                    pygame.mouse.set_visible(0)
                    holdingTile = True
            else:
                if tileGrid.isInGrid(pos):
                    if tileGrid.isPlaceableAtPos(pos):
                        tileGrid.setTileAtPos(pos, heldTile)
                    else:
                        break
                elif itemMenu.isInMenu(pos):
                    heldTile = itemMenu.getItem(pos)
                    break
                else:
                    heldTile = heldTile = tile.Tile(0, 0, 0)
                pygame.mouse.set_visible(1)
                holdingTile = False


    background.fill((250, 250, 250))
    screen.blit(background, (0, 0))
    if holdingTile:
        pos = pygame.mouse.get_pos()
        if tileGrid.isPlaceableAtPos(pos):
            heldTile.isGreyed = False
        else:
            heldTile.isGreyed = True
        x = pos[0] - math.floor(heldTile.size / 2)
        y = pos[1] - math.floor(heldTile.size / 2)
        heldTile.updatePos((x, y))
    tileGrid.draw(screen)
    itemMenu.draw(screen)
    heldTile.draw(screen)
    pygame.display.flip()
