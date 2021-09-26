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

def _move(player_x, player_y, dx, dy):

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
    draw()

def putLeaf():
    for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell == player:
                    level[test_y][test_x] = player_on_storage
                    draw()
    
def putBerry():
    putLeaf()
    
def removeLeaf():
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
        return isTreeFromKara(0, 1)   
    elif player_rotation == 'up':
        return isTreeFromKara(1, 0)
    elif player_rotation == 'left':
        return isTreeFromKara(0, -1)
    elif player_rotation == 'down':
        return isTreeFromKara(-1, 0)
    
def treeRight():
    if player_rotation == 'right':
        return isTreeFromKara(0, -1)   
    elif player_rotation == 'up':
        return isTreeFromKara(-1, 0)
    elif player_rotation == 'left':
        return isTreeFromKara(0, 1)
    elif player_rotation == 'down':
        return isTreeFromKara(1, 0)
    
def isTreeFromKara(x, y):
    player_x, player_y = find_player()
    
    return isTree(player_x + x, player_y + y)
    
def isTree(x, y):
    return level[y][x] == wall

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
    
    return isMushroom(player_x + x, player_y+ y)
    
def isMushroom(x, y):
    return level[y][x] == box or level[y][x] == box_on_storage

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
        onLeaf()
    def onBerry(self):
        onBerry()
    def treeFront(self):
        treeFront()
    def treeLeft(self):
        treeLeft()
    def treeRight(self):
        treeRight()
    def mushroomFront(self):
        mushroomFront()
    
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
                
    canvas.update() #window.mainloop()
    
    time.sleep(TIME_S)

window = tkinter.Tk()
window.title("PythonKara")
window.geometry(str(WIDTH) + 'x' + str(HEIGHT))

canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#B4E6B4")

objs = {}

draw() # initial setup