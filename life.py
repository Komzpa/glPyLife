import PyWarGame
from time import sleep
import random

size = 80

def build_board(world=[]):
    board = ""
    for line in world:
        for char in line:
            board += char
    return board


def next_state(world):
    neib = []
    for i in xrange(size+1):
        neib.append([])
        for j in xrange(size+1):
            neib[i].append(0)

# ============================================= calc neibs
    for line in xrange(1,size-1):
        for char in xrange(1,size-1):

            if world[line-1][char-1] == "x":
                neib[line][char]+=1
            if world[line-1][char] == "x":
                neib[line][char]+=1
            if world[line-1][char+1] == "x":
                neib[line][char]+=1
            if world[line][char-1] == "x":
                neib[line][char]+=1
            if world[line][char+1] == "x":
                neib[line][char]+=1
            if world[line+1][char-1] == "x":
                neib[line][char]+=1
            if world[line+1][char] == "x":
                neib[line][char]+=1
            if world[line+1][char+1] == "x":
                neib[line][char]+=1
#================================================ update state
    for line in xrange(size):
        for char in xrange(size):
            if world[line][char] != "x":
                if neib[line][char] == 3:
                    world[line][char] = "x"
            else:
                if (neib[line][char] == 2) or (neib[line][char] == 3):
                    world[line][char] = "x"
                else:
                    world[line][char] = "o"

    return world
    
def load_world(file_name):
    world_file = open(file_name, "r")
    world = []
    for line in world_file.readlines():
        world_line = [ch for ch in line]
        world_line.pop()
        world.append(world_line)
    world_file.close()
    return world

def main():
    PyWarGame.show_window("Python Life Extension", 640, 480)

    the_world = load_world("world.txt")
    print "The world ",len(the_world)," x ", len(the_world[0])

    the_board = build_board(the_world)
    print "the board ", len(the_board) 

    while True:
        PyWarGame.process()
    #    sleep(0.01)
        PyWarGame.update_board(the_board)
        the_board = build_board(next_state(the_world))

if __name__ == '__main__':
    main()
