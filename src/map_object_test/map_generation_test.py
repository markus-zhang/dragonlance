"""
    Test generation functions in game_map.py
"""
import sys
sys.path.append(".")
sys.path.append("..")

from map_objects.rectangle import Rect
from map_objects.game_map import GameMap
import config as cfg

def test_bsp_split(r: Rect):
    """
        Test split algorithm:
    """
    if r.x2 - r.x1 <= 2 * cfg.MIN_ROOM_WIDTH and r.y2 - r.y1 <= 2 * cfg.MIN_ROOM_HEIGHT:
        print("Too small to split")
    elif r.x2 - r.x1 > 2 * cfg.MIN_ROOM_WIDTH:
            # Split horizontally
            print("Split Horizontally:")
            print(f"Left: {r.x1}, {r.y1}, {int(r.x1 + (r.w / 2))}, {r.h}")
            test_bsp_split(Rect(r.x1, r.y1, r.w / 2, r.h))
            print(f"Left: {r.x1 + int(r.w / 2)}, {r.y1}, {int(r.w / 2) - 1}, {r.h}")
            test_bsp_split(Rect(r.x1 + int(r.w / 2), r.y1, r.w / 2, r.h))

    elif r.x2 - r.x1 > 2 * cfg.MIN_ROOM_WIDTH:
            # Split vertically
            print("Split Vertically:")
            print(f"Left: {r.x1}, {r.y1}, {int(r.x1 + (r.w / 2))}, {r.h}")
            print(f"Left: {r.x1 + int(r.w / 2)}, {r.y1}, {int(r.w / 2) - 1}, {r.h}")

if __name__ == "__main__":
    test_bsp_split(Rect(0, 0, 80, 45))