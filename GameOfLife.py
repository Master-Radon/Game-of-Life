#import libraries
import pygame
import numpy as np

#Grid Dimension
width, height = 640, 480
#Number of cells for line and column
nx, ny = 120,120
#Dimension of every cell
dimCW = width // nx
dimCH = height // ny
#Grid of cells
grid = np.zeros((nx, ny))

#PyGame GUI initialization
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load('glider.ico')) #icon

#initialize the grid
def init_grid(grid):
  for i in range(nx):
    for j in range(ny):
      grid[i][j] = np.random.randint(2)

#draw the grid on the screen
def draw_grid(grid, surface):
  for i in range(nx):
    for j in range(ny):
      if grid[i][j] == 1:
        color = (255, 255, 255)
      else:
        color = (0, 0, 0)
      pygame.draw.rect(surface, color, (i * dimCW, j * dimCH, dimCW, dimCH))

#count the number of living cells near every cell
def get_alive_neighbors(grid, x, y):
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      #check if the cordinates exist in the grid
      if x+i >= 0 and x+i < nx and y+j >= 0 and y+j < ny:
        if grid[x+i][y+j] == 1:
          count += 1
  return count

#update the grid following the game's rules
def update_grid(grid):
  new_grid = np.copy(grid)
  for i in range(nx):
    for j in range(ny):
      #count the number of living cells near every cell
      neighbors = get_alive_neighbors(grid, i, j)
      #update the cell status based on the neighbors cells
      if grid[i][j] == 1:
        if neighbors < 2 or neighbors > 3:
          new_grid[i][j] = 0
      else:
        if neighbors == 3:
          new_grid[i][j] = 1
  return new_grid

#initialize the grid
init_grid(grid)

#main cicle
while True:
  #manage the events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  #draw the grid on the screen
  draw_grid(grid, screen)
  pygame.display.update()
  #update the grid
  grid = update_grid(grid)
  #little delay between every operation
  pygame.time.wait(50)
