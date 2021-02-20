import pygame
import sys


def additional(a_list):
  maximum = 0

  for element in a_list:
    maximum = max(len(element), maximum)

  return maximum


class Nonogram:
  def __init__(self, x, y):
    pygame.display.set_caption('Nonogram')
    pygame.init()
    self.x = x
    self.y = y

    self.len_x = len(x)
    self.len_y = len(y)
    self.x_additional = additional(y)
    self.y_additional = additional(x)

    self.font = pygame.font.SysFont(None, 20)
    self.screen = pygame.display.set_mode((20*(self.len_x + self.x_additional), 20*(self.len_y + self.y_additional)))

    self.fields = [[0 for i in range(self.len_x)] for j in range(self.len_y)]
    print(self.fields)

  def draw(self):
    self.screen.fill((255, 255, 255))

    self.create_grid()
    self.insert_numbers()
    self.marked()
    pygame.display.update()

  def create_grid(self):
    for i in range(1, self.len_x + self.x_additional):
      pygame.draw.line(self.screen, (0, 0, 0), (20*i, 0), (20*i, 20*(self.len_y + self.y_additional)))

    for i in range(1, self.len_y + self.y_additional):
      pygame.draw.line(self.screen, (0, 0, 0), (0, 20*i), (20*(self.len_x + self.x_additional), 20*i))

    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, 0, 20*self.x_additional, 20*self.y_additional))

  def insert_numbers(self):
    for i in range(len(self.x)):
      for j in range(len(self.x[i])):
        self.screen.blit(self.font.render(str(self.x[i][j]), True, (0, 0, 0)), (20*(self.x_additional + i) + 7, 20*j + 4))

    for i in range(len(self.y)):
      for j in range(len(self.y[i])):
        self.screen.blit(self.font.render(str(self.y[i][j]), True, (0, 0, 0)), (20*j + 7, 20*(self.y_additional + i) + 4))

  def marked(self):
    for i in range(self.len_y):
      for j in range(self.len_x):
        if self.fields[i][j] == 2:
          pygame.draw.circle(self.screen, (255, 0, 0), (20*(j + self.x_additional) + 10, 20*(i + self.y_additional) + 10), 5)

        else:
          pygame.draw.rect(self.screen, (255*(1 - self.fields[i][j]), 255*(1 - self.fields[i][j]), 255*(1 - self.fields[i][j])), pygame.Rect(20*(j + self.x_additional) + 1, 20*(i + self.y_additional) + 1, 19, 19))

  def marking(self, pos, type):
    if pos[0] > 20*self.x_additional and pos[1] > 20*self.y_additional:
      self.fields[(pos[1] - 20*self.y_additional)//20][(pos[0] - 20*self.x_additional)//20] += type
      self.fields[(pos[1] - 20*self.y_additional)//20][(pos[0] - 20*self.x_additional)//20] %= 3

  def running(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

      if event.type == pygame.MOUSEBUTTONUP:
        self.marking(pygame.mouse.get_pos(), 2 - event.button)

    game.draw()


game = Nonogram([list(range(3)) for i in range(5)], [list(range(4)) for i in range(4)])
while True:
  game.running()
