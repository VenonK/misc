import pygame
import heapq

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create a Pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding Visualization")

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * SQUARE_SIZE
        self.y = col * SQUARE_SIZE
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_wall(self):
        return self.color == BLACK

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = GREEN

    def make_end(self):
        self.color = RED

    def make_wall(self):
        self.color = BLACK

    def make_path(self):
        self.color = BLUE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))

    def update_neighbors(self, grid):
        self.neighbors = []
        # Directions: up, down, left, right
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_wall():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])
        if self.col < COLS - 1 and not grid[self.row][self.col + 1].is_wall():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

# Heuristic function for A* (Manhattan Distance)
def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

# A* Algorithm
def a_star(draw, grid, start, end):
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))
    came_from = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while open_set:
        current = heapq.heappop(open_set)[2]

        if current == end:
            # Reconstruct path
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            return True

        open_set_hash.remove(current)

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

        draw()

    return False

# Create grid
def make_grid():
    return [[Node(i, j) for j in range(COLS)] for i in range(ROWS)]

# Draw grid and nodes
def draw(win, grid):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    # Draw grid lines
    for i in range(ROWS):
        pygame.draw.line(win, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE))
        pygame.draw.line(win, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT))

    pygame.display.update()

# Get mouse position on grid
def get_clicked_pos(pos):
    x, y = pos
    row = x // SQUARE_SIZE
    col = y // SQUARE_SIZE
    return row, col

# Main function
def main(win):
    grid = make_grid()

    start = None
    end = None

    run = True
    while run:
        draw(win, grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != start and node != end:
                    node.make_wall()

            elif pygame.mouse.get_pressed()[2]:  # Right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    a_star(lambda: draw(win, grid), grid, start, end)

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid()

    pygame.quit()

main(WIN)
