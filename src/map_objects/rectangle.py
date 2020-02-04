class Rect:
    def __init__(self, x, y, w, h):
        self._x1 = x
        self._y1 = y
        self._x2 = x + w
        self._y2 = y + h

    # BEGIN getters and setters

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1

    @property
    def x2(self):
        return self._x2

    @property
    def y2(self):
        return self._y2

    # END getters and setters

    # Maybe I should add the tunnels in this class, 
    # so that we only need to connect the end points of those tunnels
