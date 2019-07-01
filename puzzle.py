import random
random.seed(10)

puzzle = [  0,
           1,1,
          1,1,1,
         1,1,1,1,
        1,1,1,1,1]

moves = [ (0, 3, 1),
        (0, 5, 2),
        (1, 6, 3),
        (1, 8, 4),
        (2, 9, 5),
        (2, 7, 4),
        (3, 0, 1),
        (3, 10, 6),
        (3, 12, 7),
        (4, 11, 7),
        (4, 13, 8),
        (5, 0, 2),
        (5, 12, 8),
        (5, 14, 9),
        (6, 1, 3),
        (6, 8, 7),
        (7, 2, 4),
        (7, 9, 8),
        (8, 1, 4),
        (8, 6, 7),
        (9, 2, 5),
        (9, 7, 8),
        (10, 3, 6),
        (10, 12, 11),
        (11, 4, 7),
        (11, 13, 12),
        (12, 3, 7),
        (12, 10, 11),
        (12, 5, 8),
        (12, 14, 13),
        (13, 4, 8),
        (13, 11, 12),
        (14, 5, 9),
        (14, 12, 13)
    ]

"""
initialize the puzzle with the open spot at the top of the puzzle
"""
def init_puzzle():
    puzzle[::] = [
            0,
           1,1,
          1,1,1,
         1,1,1,1,
        1,1,1,1,1]

"""
print out the puzzle list formatted more like how the game looks.
"""
def print_puzzle():
    print("puzzle =",puzzle)
    print("     ",puzzle[0])
    print("    ", puzzle[1], puzzle[2])
    print("   ", puzzle[3], puzzle[4], puzzle[5])
    print("  ", puzzle[6], puzzle[7], puzzle[8], puzzle[9])
    print(" ", puzzle[10], puzzle[11], puzzle[12], puzzle[13], puzzle[14])

""" check if the puzzle has been solved; precisely if there are only
def solved():  if there is only one peg left.
"""
def solved():
    return sum(puzzle) == 1

"""create a list of valid moves in the form of simple tuples that define
the start and then end of the valid move.  If this list is empty then
there are no more valid moves.
"""
valid = []
def addmove(a,b):
    t = tuple()
    if puzzle[a] == 1 and puzzle[b] == 0:
        t = a,b
        valid.append(t)

def valid_moves():
    # first set should be [(3,0),(5,0)]
    del valid[::]
    addmove(0,3)
    addmove(1,6)
    addmove(1,8)
    addmove(2,7)
    addmove(2,9)
    addmove(3,0)
    addmove(3,10)
    addmove(3,12)
    addmove(4,11)
    addmove(4,13)
    addmove(5,0)
    addmove(5,12)
    addmove(5,14)
    addmove(6,1)
    addmove(6,8)
    addmove(7,2)
    addmove(7,9)
    addmove(8,1)
    addmove(8,6)
    addmove(9,2)
    addmove(9,7)
    addmove(10,3)
    addmove(10,12)
    addmove(11,4)
    addmove(11,13)
    addmove(12,3)
    addmove(12,5)
    addmove(12,10)
    addmove(12,14)
    addmove(13,4)
    addmove(13,11)
    addmove(14,12)
    addmove(14,5)
    return valid

"""
choose which move we want to use for this round
"""
def domove(t):
    a = t[0]
    b = t[1]
    puzzle[a] = 0
    puzzle[b] = 1
    if a == 0 and b == 3:
        c=1
    if a == 0 and b == 5:
        c=2
    if a == 1 and b == 6:
        c=3
    if a == 1 and b == 8:
        c=4
    if a == 2 and b == 9:
        c=5
    if a == 2 and b == 7:
        c=4
    if a == 3 and b == 0:
        c=1
    if a == 3 and b == 10:
        c=6
    if a == 3 and b == 12:
        c=7
    if a == 4 and b == 11:
        c=7
    if a == 4 and b == 13:
        c=8
    if a == 5 and b == 0:
        c=2
    if a == 5 and b == 12:
        c=8
    if a == 5 and b == 14:
        c=9
    if a == 6 and b == 1:
        c=3
    if a == 6 and b == 8:
        c=7
    if a == 7 and b == 2:
        c=4
    if a == 7 and b == 9:
        c=8
    if a == 8 and b == 1:
        c=4
    if a == 8 and b == 6:
        c=7
    if a == 9 and b == 2:
        c=5
    if a == 9 and b == 7:
        c=8
    if a == 10 and b == 3:
        c=6
    if a == 10 and b == 12:
        c=11
    if a == 11 and b == 4:
        c=7
    if a == 11 and b == 13:
        c=12
    if a == 12 and b == 3:
        c=7
    if a == 12 and b == 10:
        c=11
    if a == 12 and b == 5:
        c=8
    if a == 12 and b == 14:
        c=13
    if a == 13 and b == 4:
        c=8
    if a == 13 and b == 11:
        c=12
    if a == 14 and b == 5:
        c=9
    if a == 14 and b == 12:
        c=13

    puzzle[c] = 0
    
def choose_move():
    print ("Moves: ", valid)
    l=len(valid)-1
    s=random.randint(0,l)
    print ("Length: ",l,", Selector: ",s)
    move = valid[s]
    print ("Move ",move)
    if move[0] != 1 and move[1] != 0:
        print("Bad Move Specified", move)
        return False
    domove(move)
    return False

#####################################################################
#  Start solver...
#####################################################################
init_puzzle()
print_puzzle()
print ("Solved? ", solved())
loops = 0
while valid_moves():
    loops = loops + 1
    print ("Loop: ", loops)
    choose_move()
    if solved():
        print ("Puzzle solved!")
        break
    if loops > 10:
        print ("Solver Loops Exceeded")
        break
    print_puzzle()

if not solved():
    print ("Puzzle not solved and no valid moves left.")
print_puzzle()