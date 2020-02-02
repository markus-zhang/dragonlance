from map_objects.tile import Tile

class GameMap:
    def __init__(self, width: int, height: int):
        self._width: int = width
        self._height: int = height
        self._tiles = self.initialize_tiles()

    # BEGIN getters and setters

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def tiles(self):
        return self._tiles

    # END getters and setters

    def initialize_tiles(self):
        tiles = [[Tile(False) for y in range(self._height)] for x in range(self._width)]

        tiles[30][22].blocked = True
        tiles[31][22].blocked = True
        tiles[32][22].blocked = True
        tiles[30][22].block_sight = True
        tiles[31][22].block_sight = True
        tiles[32][22].block_sight = True

        return tiles

    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked

