import pygame as pg
import numpy as np


class MapaNode:

    def __init__(self, position, parent=None):
        self.parent = parent
        self.position = position

    def __eq__(self, other):
        return self.position[0] == other.position[0] and self.position[
            1] == other.position[1]


class deepSearch(object):

    def run(self, mapa, start, end):
        mapa = mapa.astype(np.float)
        startNode = MapaNode(start[::-1])
        endNode = MapaNode(end[::-1])
        path = []
        pila = []
        pila.append(startNode)
        mapaRows, mapaCols = np.shape(mapa)
        visited = np.zeros(mapa.shape)
        while (len(pila) != 0):
            currentNode = pila.pop()
            if currentNode == endNode:
                break

            movements = [[-1, -1, 1.4], [0, -1, 1], [1, -1, 1.4], [-1, 0, 1],
                         [1, 0, 1], [-1, 1, 1.4], [0, 1, 1], [1, 1, 1.4]]

            movements = [[0, -1, 1], [-1, 0, 1], [1, 0, 1], [0, 1, 1]]

            for movement in movements:

                newPosition = [
                    currentNode.position[0] + movement[0],
                    currentNode.position[1] + movement[1]
                ]

                if newPosition[0] < 0 or newPosition[1] < 0 or newPosition[
                        1] >= mapaCols or newPosition[0] >= mapaRows:
                    continue
                elif visited[newPosition[0]][newPosition[1]] == 1:
                    continue
                elif mapa[newPosition[0]][newPosition[1]] == 0:
                    continue
                else:

                    adjacentNode = MapaNode(newPosition, currentNode)
                    pila.append(adjacentNode)
                    visited[newPosition[0]][newPosition[1]] = 1

        while currentNode is not None:
            path.append(currentNode.position)
            currentNode = currentNode.parent
        return path, visited


class breadthSearch(object):

    def run(self, mapa, start, end):
        mapa = mapa.astype(np.float)
        startNode = MapaNode(start[::-1])
        endNode = MapaNode(end[::-1])
        path = []
        cola = []
        cola.append(startNode)
        mapaRows, mapaCols = np.shape(mapa)
        visited = np.zeros(mapa.shape)
        while (len(cola) != 0):
            currentNode = cola.pop(0)
            if currentNode == endNode:
                break

            movements = [[-1, -1, 1.4], [0, -1, 1], [1, -1, 1.4], [-1, 0, 1],
                         [1, 0, 1], [-1, 1, 1.4], [0, 1, 1], [1, 1, 1.4]]

            movements = [[0, -1, 1], [-1, 0, 1], [1, 0, 1], [0, 1, 1]]

            for movement in movements:

                newPosition = [
                    currentNode.position[0] + movement[0],
                    currentNode.position[1] + movement[1]
                ]

                if newPosition[0] < 0 or newPosition[1] < 0 or newPosition[
                        1] >= mapaCols or newPosition[0] >= mapaRows:
                    continue
                elif visited[newPosition[0]][newPosition[1]] == 1:
                    continue
                elif mapa[newPosition[0]][newPosition[1]] == 0:
                    continue
                else:

                    adjacentNode = MapaNode(newPosition, currentNode)
                    cola.append(adjacentNode)
                    visited[newPosition[0]][newPosition[1]] = 1

        while currentNode is not None:
            path.append(currentNode.position)
            currentNode = currentNode.parent
        return path, visited


pg.init()
#mapaAlg = np.load('mapaProfundidad2.npy')
mapaAlg=np.load('mapaProfundidad.npy')
width, height = mapaAlg.shape
BLACK = pg.Color('#16213E')
WHITE = pg.Color('#FFF9D7')
GREEN = pg.Color('#533483')
RED = pg.Color('#E94560')
BLUE = pg.Color('#E94560')
color_light = (170, 170, 170)

color_dark = (100, 100, 100)
smallfont = pg.font.SysFont('arial', 30)
text = smallfont.render('Pushale', True, RED)
tile_size = 10
start = [10, 3]
goal = [5, 30]
topPadding = 50
#search=breadthSearch()
search = deepSearch()

screen = pg.display.set_mode(
    (width * tile_size, height * tile_size + topPadding))
clock = pg.time.Clock()

background = pg.Surface((width * tile_size, height * tile_size))
buttons = pg.Surface((width * tile_size, 50))

for y in range(0, height):
    for x in range(0, width):
        rect = (x * tile_size, y * tile_size, tile_size, tile_size)
        if (mapaAlg[y, x] == 0):
            color = BLACK
        else:
            color = WHITE
        if x == start[0] and y == start[1]:
            color = GREEN
        if x == goal[0] and y == goal[1]:
            color = RED
        pg.draw.rect(background, color, rect)

game_exit = False
while not game_exit:
    mouse = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if event.type == pg.MOUSEBUTTONDOWN:

            if 10 <= mouse[0] <= 150 and 10 <= mouse[1] <= 40:
                camino, mapavisited = search.run(mapaAlg, start, goal)
                for point in camino:
                    rect = (point[1] * tile_size, point[0] * tile_size,
                            tile_size, tile_size)
                    pg.draw.rect(background, BLUE, rect)

    if 0 <= mouse[0] <= 140 and 10 <= mouse[1] <= 40:
        pg.draw.rect(buttons, color_light, [10, 10, 140, 30])

    else:
        pg.draw.rect(buttons, color_dark, [10, 10, 140, 30])

    screen.fill((0, 0, 0))

    screen.blit(buttons, (0, 0))
    screen.blit(background, (0, 50))
    screen.blit(text, (10, 10))
    pg.display.flip()
    clock.tick(30)
pg.display.quit()