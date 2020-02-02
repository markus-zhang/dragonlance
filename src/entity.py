class Entity:
    """
    Base Class that represents the players, monsters, etc.
    """
    def __init__(self, x, y, char, color):
        self._x = x
        self._y = y
        self._char = char
        self._color = color

    # BEGIN getters and setters

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
            self._y = y

    # END getters and setters
    
    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    
