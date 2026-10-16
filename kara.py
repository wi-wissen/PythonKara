import copy
import tkinter
import time

player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '

if 'levels' not in globals(): levels = [
        """
  ###
  #.#
  # ####
###$ $.#
#. $@###
####$#
   #.#
   ###
        """
    ,
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
]

CELL_SIZE = 32
HEIGHT = CELL_SIZE * 16
WIDTH = CELL_SIZE * 16
if 'TIME_S' not in globals(): TIME_S = 0.5
if 'STRICT' not in globals(): STRICT = True

level = []
if 'current_level' not in globals(): current_level = 0
player_rotation = 'up'
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
    
    #find max
    offset_y = len(level)-1
    offset_x = 0
    for line in level:
        if len(line)-1 > offset_x: offset_x = len(line)-1
        
    #add missing empty fields if needed
    for index, line in enumerate(level):
        diff = int(offset_x - (len(line)-1))
        if(diff > 0):
            for i in range(diff):
                level[index].append(' ')
    
    #cell to pixel
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

def turnRight():
    global player_rotation
    
    if player_rotation == 'right':
        player_rotation = 'down'
    elif player_rotation == 'down':
        player_rotation = 'left'
    elif player_rotation == 'left':
        player_rotation = 'up'
    elif player_rotation == 'up':
        player_rotation = 'right'
        
    draw()
        
def turnLeft():
    global player_rotation
    
    if player_rotation == 'right':
        player_rotation = 'up'
    elif player_rotation == 'up':
        player_rotation = 'left'
    elif player_rotation == 'left':
        player_rotation = 'down'
    elif player_rotation == 'down':
        player_rotation = 'right'
        
    draw()

def move():
    global current_level
    
    player_x, player_y = find_player()

    dx = 0
    dy = 0
    
    if player_rotation == 'right':
        dx = 1
    elif player_rotation == 'up':
        dy = -1
    elif player_rotation == 'left':
        dx = -1
    elif player_rotation == 'down':
        dy = 1

    _move(player_x, player_y, dx, dy)

def _field(x, y):
    # Returns the coordinates of field (x, y) or None if it is outside of the world.
    # Without STRICT the world wraps around, so every field exists.
    if not STRICT:
        return x % len(level[0]), y % len(level)
    if 0 <= y < len(level) and 0 <= x < len(level[y]):
        return x, y
    return None

def _move(player_x, player_y, dx, dy):
    global level, STRICT

    next_field = _field(player_x + dx, player_y + dy)
    if next_field is None:
        raise Exception('Kara can not leave the world.')
    next_x, next_y = next_field

    current = level[player_y][player_x] #kara or kara on kara on berry
    adjacent = level[next_y][next_x] # next field
    beyond = ''
    beyond_field = _field(next_x + dx, next_y + dy)
    if beyond_field is not None:
        beyond_x, beyond_y = beyond_field
        beyond = level[beyond_y][beyond_x]

    #define next states
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

    if adjacent in next_adjacent: # next field
        level[player_y][player_x] = next_current[current]
        level[next_y][next_x] = next_adjacent[adjacent]

    elif beyond in next_beyond and adjacent in next_adjacent_push: # field after next field
        level[player_y][player_x] = next_current[current]
        level[next_y][next_x] = next_adjacent_push[adjacent]
        level[beyond_y][beyond_x] = next_beyond[beyond]
        
    elif STRICT: #can't move
        raise Exception('Kara bumped into a tree.')
        
    is_level_complete()
    draw()

def putLeaf():
    if STRICT and onLeaf():
        raise Exception('Kara can not put down a berry, there is already one.')
    for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player:
                    level[test_y][test_x] = player_on_storage
                    draw()

def putBerry():
    putLeaf()

def removeLeaf():
    if STRICT and not onLeaf():
        raise Exception('Kara can not pick up a berry, there is none.')
    for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player_on_storage:
                    level[test_y][test_x] = player
                    draw()
    
def removeBerry():
    removeLeaf();
 
def onLeaf():
    for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player_on_storage:
                    return True
    
    return False
    
def onBerry():
    return onLeaf();
    
def treeFront():
    if player_rotation == 'right':
        return isTreeFromKara(1, 0)
    elif player_rotation == 'up':
        return isTreeFromKara(0, -1)
    elif player_rotation == 'left':
        return isTreeFromKara(-1, 0)
    elif player_rotation == 'down':
        return isTreeFromKara(0, 1)
    
def treeLeft():
    if player_rotation == 'right':
        return isTreeFromKara(0, -1)   
    elif player_rotation == 'up':
        return isTreeFromKara(-1, 0)
    elif player_rotation == 'left':
        return isTreeFromKara(0, 1)
    elif player_rotation == 'down':
        return isTreeFromKara(1, 0)
    
def treeRight():
    if player_rotation == 'right':
        return isTreeFromKara(0, 1)   
    elif player_rotation == 'up':
        return isTreeFromKara(1, 0)
    elif player_rotation == 'left':
        return isTreeFromKara(0, -1)
    elif player_rotation == 'down':
        return isTreeFromKara(-1, 0)
    
def isTreeFromKara(x, y):
    player_x, player_y = find_player()
    field = _field(player_x + x, player_y + y)
    if field is None:
        return False #no field

    return isTree(*field)

def isTree(x, y):
    if 0 <= y < len(level) and 0 <= x < len(level[y]):
        return level[y][x] == wall
    else:
        return False; #no field

def mushroomFront():
    if player_rotation == 'right':
        return isMushroomFromKara(1, 0)
    if player_rotation == 'up':
        return isMushroomFromKara(0, -1)
    if player_rotation == 'left':
        return isMushroomFromKara(-1, 0)
    if player_rotation == 'down':
        return isMushroomFromKara(0, 1)
    
def isMushroomFromKara(x, y):
    player_x, player_y = find_player()
    field = _field(player_x + x, player_y + y)
    if field is None:
        return False #no field

    return isMushroom(*field)

def isMushroom(x, y):
    if 0 <= y < len(level) and 0 <= x < len(level[y]):
        return level[y][x] == box or level[y][x] == box_on_storage
    else:
        return False; #no field

class Kara:
    def move(self):
        move()
    def turnRight(self):
        turnRight()
    def turnLeft(self):
        turnLeft()
    def putLeaf(self):
        putLeaf()
    def putBerry(self):
        putBerry()
    def removeLeaf(self):
        removeLeaf()
    def removeBerry(self):
        removeBerry()
    def onLeaf(self):
        return onLeaf()
    def onBerry(self):
        return onBerry()
    def treeFront(self):
        return treeFront()
    def treeLeft(self):
        return treeLeft()
    def treeRight(self):
        return treeRight()
    def mushroomFront(self):
        return mushroomFront()
    
kara = Kara()


def is_level_complete():
    global current_level
    
    complete = True

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == box:
                complete = False

    return complete

def draw():
    global window, canvas, objs
    
    # clean up
    canvas.delete("all")
    
    # background
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#B4E6B4")
    
    #grid
    cells_y = len(level)-1
    cells_x = 0
    for line in level:
        if len(line)-1 > cells_x: cells_x = len(line)-1
        
    for y in range(cells_y+2):
        canvas.create_line(
            (offset_x - CELL_SIZE/2, offset_y + y * CELL_SIZE - CELL_SIZE/2), #start
            (offset_x + (cells_x+1) * CELL_SIZE - CELL_SIZE/2, offset_y + y * CELL_SIZE - CELL_SIZE/2), #end
            fill="#90b890" #rgb(144,184,144)
        ) 
        
    for x in range(cells_x+2):    
        canvas.create_line(
            (offset_x + x * CELL_SIZE - CELL_SIZE/2, offset_y - CELL_SIZE/2), #start
            (offset_x + x * CELL_SIZE - CELL_SIZE/2, offset_y + (cells_y+1) * CELL_SIZE - CELL_SIZE/2), #end
            fill="#90b890" #rgb(144,184,144)
        )
    
    #figures
    objs = {}
    i = 0
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell != empty:
                   
                if cell == player_on_storage or cell == box_on_storage:
                    objs[str(i)+'storage'] = tkinter.PhotoImage(file=r'images/strawberry.png')
                    canvas.create_image(offset_x + x * CELL_SIZE, offset_y + y * CELL_SIZE, image=objs[str(i)+'storage'], anchor="center")
                    
                if cell == player or cell == player_on_storage:
                    objs[i] = tkinter.PhotoImage(file=r'images/ladybug-' + player_rotation + '.png')
                elif cell == box or cell == box_on_storage:
                    objs[i] = tkinter.PhotoImage(file=r'images/mushroom-single.png')
                elif cell == storage:
                    objs[i] = tkinter.PhotoImage(file=r'images/strawberry.png')
                elif cell == wall:
                    objs[i] = tkinter.PhotoImage(file=r'images/forest.png')
                
                canvas.create_image(offset_x + x * CELL_SIZE, offset_y + y * CELL_SIZE, image=objs[i], anchor="center")
                
                i += 1
                
    canvas.update()
    
    time.sleep(TIME_S)

window = tkinter.Tk()
window.title("PythonKara")
window.geometry(str(WIDTH) + 'x' + str(HEIGHT))

icon = tkinter.PhotoImage(file=r'images/ladybug-right.png')
window.iconphoto(False, icon)

# init window
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

objs = {}

# add key bindings
def on_key_press(event):
    if event.keysym == 'Up':
        move()
    elif event.keysym == 'Left':
        turnLeft()
    elif event.keysym == 'Right':
        turnRight()
    elif event.keysym == 'space':
        if onLeaf():
            removeLeaf()
        else:
            putLeaf()

window.bind('<KeyPress>', on_key_press)
window.focus_set()

# initial setup
draw()