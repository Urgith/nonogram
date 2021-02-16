import pygame


def draw(okno_gry, x, y):
  okno_gry.fill((255, 255, 255))

  for i in range(len(x)):
    pygame.draw.line(okno_gry, (0, 0, 0), (20*(i + 1), 0), (20*(i + 1), 20*len(y)))

  for i in range(len(y)):
    pygame.draw.line(okno_gry, (0, 0, 0), (0, 20*(i + 1)), (20*len(x), 20*(i + 1)))


def nonogram(x, y):
  pygame.init()
  okno_gry = pygame.display.set_mode((20*len(x), 20*len(y)))
  pygame.display.set_caption('Nonogram')

  font = pygame.font.SysFont(None, 5)

  loop = True
  while loop:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        loop = False

    draw(okno_gry, x, y)
    pygame.display.update()


nonogram([list(range(5)) for i in range(5)], [list(range(5)) for i in range(5)])
