"""
    Test generation functions in game_map.py
"""
from map_objects.rectangle import Rect
from map_objects.game_map import GameMap
import config as cfg

def test_bsp_split(r: Rect):
    """
        Test split algorithm:
        1. Only test one split
        2. 
    """
    if r.x2 - r.x1 <= 2 * cfg.MIN_ROOM_WIDTH & r.y2 - r.y1 <= 2 * cfg.MIN_ROOM_HEIGHT:
        print("Too small to split")
    else:
        if r.x2 - r.x1 > 2 * cfg.MIN_ROOM_WIDTH:
            # Split horizontally
            print("Split Horizontally:")
            print(f"Left: {r.x1}, {r.y1}, {int(r.w / 2)}, {r.h}")
            print(f"Left: {r.x1 + int(r.w / 2) + 1}, {r.y1}, {int(r.w / 2)}, {r.h}")
    pass

if __name__ == "__main__":
    test_bsp_split(Rect(0, 0, 8, 6))