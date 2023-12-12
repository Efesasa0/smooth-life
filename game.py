import numpy as np

class Cell:
    def __init__(self, x: int, y: int, state: int = 0) -> None:
        self.x = x
        self.y = y
        self.state = state

    def __str__(self) -> str:
        return f"coords: ({self.x},{self.y}) state:{self.status}\n"

class Environment:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.grid = np.empty((height,width),dtype=Cell)
        for x in range(width):
            for y in range(height):
                self.grid[y][x]=Cell(x,y,0)

    def __str__(self) -> None:
        return f"{self.grid}"