from map_objects.tile import Tile
from map_objects.rectangle import Rect
import config as cfg

class GameMap:
    def __init__(self, width: int, height: int):
        self._width: int        = width
        self._height: int       = height
        self._tiles: list       = self.initialize_tiles()
        self._num_rooms: int    = 0

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

    @property
    def num_rooms(self):
        return self._num_rooms

    # END getters and setters

    # BEGIN dungeon random generation algorithms
    """
    Please note that we will import prefabs from another module,
    so that we can mix them with random generated tiles
    """

    # First two are just example funtions
    def create_room(self, room: Rect, tiles):
        # go through the tiles in the rectangle and make them passable
        for y in range(room.y1 + 1, room.y2):
            for x in range(room.x1 + 1, room.x2):
                tiles[x][y].blocked = False
                tiles[x][y].block_sight = False

    def make_map(self, tiles):
        room1: Rect = Rect(20, 15, 10, 15)
        room2: Rect = Rect(35, 15, 10, 15)

        self.create_room(room1, tiles)
        self.create_room(room2, tiles)

    # Let's get a bit seious
    def rooms_generator_bsp(self, max_num: int):
        """
        Generate max_num rooms using BSP
        """
        self.rooms_generator_bsp_helper(max_num, 0, 0, self.width, self.height)

    def rooms_generator_bsp_helper(self, max_num: int, x: int, y: int, w: int, h: int):
        # The recursive helper function
        """ 
            Stopping criteria:
            1. Reaches maximum number of rooms
            2. The sub space is smaller than (2 * MIN_ROOM_WIDTH) * (2 * MIN_ROOM_HEIGHT)
        """
        if self.num_rooms >= cfg.MAX_ROOM_NUM:
            return

        if w <= 2 * cfg.MIN_ROOM_WIDTH & h <= 2 * cfg.MIN_ROOM_HEIGHT:
            # Make a room
            self.create_room(Rect(x, y, w, h), self.tiles)

        """
            Recursively split the rectangle:
            1. If width >= 2 * MIN_ROOM_WIDTH, split width
            2. If height >= 2 * MIN_ROOM_HEIGHT, split height
        """
        if w >= 2 * cfg.MIN_ROOM_WIDTH:
            self.rooms_generator_bsp_helper(max_num, x, y, int(w / 2), h)
            self.rooms_generator_bsp_helper(max_num, x + int(w / 2) + 1, y, int(w / 2), h)
            
        elif h >= 2 * cfg.MIN_ROOM_HEIGHT:
            self.rooms_generator_bsp_helper(max_num, x, y, w, int(h / 2))
            self.rooms_generator_bsp_helper(max_num, x, y + int(h / 2) + 1, w, int(h / 2))


    # END dungeon random generation algorithms

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self._height)] for x in range(self._width)]

        # Call random generation algorithm here
        self.make_map(tiles)

        return tiles

    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked

