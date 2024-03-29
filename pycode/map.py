from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32
import random

_ = False

def r1(s):
    global _
    if s == "_":
        return _
    return s

c = str(random.randint(1, 3))
s = "map/" + c + ".txt"
f = open(s, "r")
matrix_map = []
for i in f:
    matrix_map.append(list(map(r1, i.split(", "))))

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
mini_map = set()
collision_walls = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == "1":
                world_map[(i * TILE, j * TILE)] = 1
            elif char == "2":
                world_map[(i * TILE, j * TILE)] = 2
            elif char == "3":
                world_map[(i * TILE, j * TILE)] = 3
            elif char == "4":
                world_map[(i * TILE, j * TILE)] = 4