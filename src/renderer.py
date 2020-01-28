import tcod as libtcod
from entity import Entity

class Renderer:
    """
    Renderer object
    """
    def __init__(self, fontfile: str = './asset/arial10x10.png'):
        self._fontfile = fontfile
        self.init()

    def init(self):
        libtcod.console_set_custom_font(self._fontfile, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)


    def clean_entity(self, con, entity: Entity):
        libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)

    def clean_all(self, con, entities: list):
        for entity in entities:
            self.clean_entity(con, entity)

    def draw_entity(self, con, entity: Entity):
        libtcod.console_set_default_foreground(con, entity.color)
        libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

    def draw_entities(self, con, entities: list):
        for entity in entities:
            self.draw_entity(con, entity)