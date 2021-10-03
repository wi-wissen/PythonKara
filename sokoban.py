# require https://pygame-zero.readthedocs.io/en/stable/ide-mode.html
import copy
from levels import *

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

CELL_SIZE = 32
HEIGHT = CELL_SIZE * 16
WIDTH = CELL_SIZE * 16
GAME_MODE = 'kara' # sokoban, kara

level = []
current_level = 0
player_angle = 0
offset_x = 0
offset_y = 0

def load_level():
    global level, offset_x, offset_y
    
    level = copy.deepcopy(levels[current_level])
    if(str == type(level)):
        level = level.splitlines()
        for index, line in enumerate(level):
            level[index] = list(line)
        level = level[1:len(level)-1]
    
    offset_y = len(level)-1
    offset_x = 0
    for line in level:
        if len(line)-1 > offset_x: offset_x = len(line)-1
    offset_y = (HEIGHT - offset_y * CELL_SIZE) / 2
    offset_x = (WIDTH - offset_x * CELL_SIZE) / 2

load_level()


def find_player():
    for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player or cell == player_on_storage:
                    player_x = test_x
                    player_y = test_y
                    
    return player_x, player_y

def on_key_down(key):
    global current_level, player_angle
    
    player_x, player_y = find_player()

    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):

        dx = 0
        dy = 0
        
        if GAME_MODE == 'sokoban':
            if key == keys.LEFT:
                dx = -1
                player_angle = 90
            elif key == keys.RIGHT:
                dx = 1
                player_angle = -90
            elif key == keys.UP:
                dy = -1
                player_angle = 0
            elif key == keys.DOWN:
                dy = 1
                player_angle = 180
                
        elif GAME_MODE == 'kara':
            if key == keys.LEFT:
                player_angle = (player_angle + 90) % 360
            elif key == keys.RIGHT:
                player_angle = (player_angle - 90) % 360
            elif key == keys.UP:
                if player_angle == 90:
                    dx = -1
                elif player_angle == 270:
                    dx = 1
                elif player_angle == 0:
                    dy = -1
                elif player_angle == 180:
                    dy = 1
            elif key == keys.DOWN:
                player_angle = (player_angle + 180) % 360
        change_level_state(player_x, player_y, dx, dy)
        
    elif key == keys.R:
        load_level()

    elif key == keys.N:
        current_level += 1
        if current_level >= len(levels):
            current_level = 0
        load_level()

    elif key == keys.P:
        current_level -= 1
        if current_level < 0:
            current_level = len(levels) - 1
        load_level()

def change_level_state(player_x, player_y, dx, dy):
    global current_level, player_angle

    current = level[player_y][player_x]
    adjacent = level[player_y + dy][player_x + dx]
    beyond = ''
    if (
        0 <= player_y + dy + dy < len(level)
        and 0 <= player_x + dx + dx < len(level[player_y + dy + dy])
    ):
        beyond = level[player_y + dy + dy][player_x + dx + dx]

    next_adjacent = {
        empty: player,
        storage: player_on_storage,
    }
    next_current = {
        player: empty,
        player_on_storage: storage,
    }
    next_beyond = {
        empty: box,
        storage: box_on_storage,
    }
    next_adjacent_push = {
        box: player,
        box_on_storage: player_on_storage,
    }

    if adjacent in next_adjacent:
        level[player_y][player_x] = next_current[current]
        level[player_y + dy][player_x + dx] = next_adjacent[adjacent]

    elif beyond in next_beyond and adjacent in next_adjacent_push:
        level[player_y][player_x] = next_current[current]
        level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
        level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]
        
    is_level_complete()

def is_level_complete():
    global current_level
    
    complete = True

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == box:
                complete = False

    if complete:
        current_level += 1
        if current_level >= len(levels):
            current_level = 0
        load_level()

def draw():
    #background
    screen.fill((180, 230, 180))
    
    #grid
    cells_y = len(level)-1
    cells_x = 0
    for line in level:
        if len(line)-1 > cells_x: cells_x = len(line)-1
        
    print(level)
    print(cells_y)
    print(cells_x)
    for y in range(cells_y+2):
        screen.draw.line(
            (offset_x - CELL_SIZE/2, offset_y + y * CELL_SIZE - CELL_SIZE/2), #start
            (offset_x + (cells_x+1) * CELL_SIZE - CELL_SIZE/2, offset_y + y * CELL_SIZE - CELL_SIZE/2), #end
            (144,184,144), # (r,g,b)
        ) 
        
    for x in range(cells_x+2):    
        screen.draw.line(
            (offset_x + x * CELL_SIZE - CELL_SIZE/2, offset_y - CELL_SIZE/2), #start
            (offset_x + x * CELL_SIZE - CELL_SIZE/2, offset_y + (cells_y+1) * CELL_SIZE - CELL_SIZE/2), #end
            (144,184,144), # (r,g,b)
        )    
    
    #figures
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                
                images = {
                    player: 'ladybug',
                    player_on_storage: 'ladybug_on_strawberry',
                    box: 'mushroom-single',
                    box_on_storage: 'mushroom-single_on_strawberry',
                    storage: 'strawberry',
                    wall: 'forest',
                }
                player_states = [player, player_on_storage]
                
                obj = Actor(images[cell])
                if cell in player_states: obj.angle = player_angle
                obj.pos = offset_x + x * CELL_SIZE, offset_y + y * CELL_SIZE
                
                obj.draw()
                