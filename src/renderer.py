import tcod as libtcod
from entity import Entity
from map_objects.game_map import GameMap

class Renderer:
    """
    Renderer object
    """
    def __init__(self, width: int, height: int, fontfile: str = './asset/arial10x10.png'):
        self._fontfile = fontfile
        self._width = width
        self._height = height
        self.init()

    def init(self):
        libtcod.console_set_custom_font(self._fontfile, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)


    def clear_entity(self, con, entity: Entity):
        libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)

    def clear_all(self, con, entities: list):
        for entity in entities:
            self.clear_entity(con, entity)

    def draw_entity(self, con, entity: Entity):
        libtcod.console_set_default_foreground(con, entity.color)
        libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

    def draw_entities(self, con, entities: list):
        for entity in entities:
            self.draw_entity(con, entity)

        libtcod.console_blit(con, 0, 0, self._width, self._height, 0, 0, 0)

    def draw_map(self, con, game_map: GameMap, colors: dict):
        for y in range(game_map._height):
            for x in range(game_map._width):
                if game_map._tiles[x][y]._block_sight:
                    libtcod.console_set_char_background(
                        con, x, y, 
                        colors.get('dark_wall'),
                        libtcod.BKGND_SET
                    )
                else:
                    libtcod.console_set_char_background(
                        con, x, y, 
                        colors.get('dark_ground'),
                        libtcod.BKGND_SET
                    )