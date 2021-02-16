import pygame


def additional(analyzed_list):
  maximum = 0

  for element in analyzed_list:
    length = len(element)

    if length > maximum:
      maximum = length

  return maximum


class Nonogram:
  def __init__(self, x, y):
    pygame.display.set_caption('Nonogram')
    pygame.init()

    self.x_additional = additional(x)
    self.y_additional = additional(y)
    self.x = x
    self.y = y

    self.okno_gry = pygame.display.set_mode((20*(len(x) + self.x_additional), 20*(len(y) + self.y_additional)))
    self.font = pygame.font.SysFont(None, 25)

    self.loop = True
    while self.loop:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.loop = False

      self.draw()

  def draw(self):
    self.okno_gry.fill((255, 255, 255))

    for i in range(len(self.x) + self.x_additional):
      if i < self.x_additional - 1:
          pygame.draw.line(self.okno_gry, (0, 0, 0), (20*(i + 1), 20*self.x_additional), (20*(i + 1), 20*(len(self.y) + self.y_additional)))
          continue

      pygame.draw.line(self.okno_gry, (0, 0, 0), (20*(i + 1), 0), (20*(i + 1), 20*(len(self.y) + self.y_additional)))

    for i in range(len(self.y) + self.y_additional):
      if i < self.y_additional - 1:
          pygame.draw.line(self.okno_gry, (0, 0, 0), (20*self.y_additional, 20*(i + 1)), (20*(len(self.x) + self.x_additional), 20*(i + 1)))
          continue

      pygame.draw.line(self.okno_gry, (0, 0, 0), (0, 20*(i + 1)), (20*(len(self.x) + self.x_additional), 20*(i + 1)))

    self.inserting_numbers()
    pygame.display.update()

  def inserting_numbers(self):
    for i in range(len(self.x)):
      for j in range(len(self.x[i])):
        self.okno_gry.blit(self.font.render(str(self.x[i][j]), True, (0, 0, 0)), (20*(self.x_additional + i) + 5, 20*j + 5))

    for i in range(len(self.y)):
      for j in range(len(self.y[i])):
        self.okno_gry.blit(self.font.render(str(self.y[i][j]), True, (0, 0, 0)), (20*j + 5, 20*(self.y_additional + i) + 5))


Nonogram([list(range(4)) for i in range(5)], [list(range(4)) for i in range(5)])
