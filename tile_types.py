from typing import Tuple
import numpy as np

# Tile graphics type compatible with the type from tcod.console.Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Character to display
        ("fg", "3B"),  # foreground color
        ("bg", "3B"),  # background color
    ]
)

# Tiles struct for static tile data
tile_dt = np.dtype(
    [
        ("walkable", bool),  # Is tile walkable
        ("transparent", bool),  # Is tile blocking FOV
        ("dark", graphic_dt),  # graphics for not in FOV
    ]
)


def new_tile(
        *,  # Enforce the use of keywords
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper funtion for defining individual tile types"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)), )
wall = new_tile(walkable=False, transparent=False, dark=(ord(" "), (255,255,255),(0,0,100)),)
