import pygame
from copy import deepcopy

ALIVE = (100,255,100)
DEAD = (50,50,50)
GRID = (200,200,200)
#Wiill always be square
class Grid:
	def __init__(self,size, cell_size=70):
		self.rows = size
		self.cols = size
		self.cell_size = cell_size
		self.cells = [ [False for j in range(self.cols)] for i in range(self.rows)]

	def Update(self):
		temp = deepcopy(self.cells)
		for row in range(self.rows):
			for col in range(self.cols):
				count = self.getCount(row,col)

				if self.cells[row][col] and count < 2 or count > 3: temp[row][col] = False
				if not self.cells[row][col] and count == 3: temp[row][col] = True 
		self.cells = temp


	def Draw(self, screen):
		for row in range(self.rows):
			for col in range(self.cols):
				colour = ALIVE if self.cells[row][col] else DEAD
				pygame.draw.rect(screen, colour, (row * self.cell_size, col *  self.cell_size,  self.cell_size,  self.cell_size) )
		self.drawGrid(screen)

	def drawGrid(self,screen):
		for row in range(self.rows+1):
			pygame.draw.line(screen, GRID, (row * self.cell_size, 0), (row * self.cell_size, self.rows * self.cell_size), 4 )
			pygame.draw.line(screen, GRID, (0, row * self.cell_size), (self.rows * self.cell_size, row * self.cell_size), 4 )


	def getCount(self, row, col):
		count = 0
		for dx in (-1,0,1):
			for dy in (-1,0,1):
				if not (dy == 0 and dx == 0):
					x = row + dx
					if x >= self.rows: x = 0 
					if x < 0: x = self.rows - 1

					y = col + dy
					if y >= self.cols: y = 0 
					if y < 0: y = self.cols - 1

					if self.cells[x][y]: count+=1 
		return count
					



display_size = (800,800)
tick_length = 10
# Pygame init
pygame.init()
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

num_squares = 15
grid = Grid(num_squares, display_size[0]/num_squares)
grid.cells[4][3] = True
grid.cells[4][4] = True
grid.cells[4][5] = True
grid.cells[3][5] = True
grid.cells[2][4] = True



while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True
			pygame.quit()

	

	grid.Draw(screen)
	grid.Update()

	pygame.display.flip()

	clock.tick(tick_length)