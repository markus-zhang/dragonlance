class Entity:
    """
    Base Class that represents the players, monsters, etc.
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
