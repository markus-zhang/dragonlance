import tcod as libtcod
from input import handle_key_pressed
from entity import Entity
from renderer import Renderer
from map_objects.game_map import GameMap

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    colors = {
        'dark_wall':    libtcod.Color(0, 0 ,100),
        'dark_ground':  libtcod.Color(50, 50, 150)
    }

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    player = Entity(player_x, player_y, '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]
    render = Renderer(screen_width, screen_height, './asset/arial10x10.png')

    libtcod.console_set_custom_font(render._fontfile, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'Dragonlance', False)
    con = libtcod.console_new(screen_width, screen_height)

    game_map = GameMap(map_width, map_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
        # libtcod.console_put_char(con, player.x, player.y, player.char, libtcod.BKGND_NONE)

        # libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        # libtcod.console_set_default_foreground(0, libtcod.white)
        # libtcod.console_put_char(0, player.x, player.y, player.char, libtcod.BKGND_NONE)
        render.draw_map(con, game_map, colors)
        render.draw_entities(con, entities)
        libtcod.console_flush()

        # libtcod.console_put_char(con, player.x, player.y, ' ', libtcod.BKGND_NONE)
        # libtcod.console_put_char(0, player.x, player.y, ' ', libtcod.BKGND_NONE)
        render.clear_all(con, entities)

        action: dict = handle_key_pressed(key)
        move = action.get('move')
        fullscreen = action.get('fullscreen')
        exit = action.get('exit')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
        
        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        
        

if __name__ == '__main__':
    main()
