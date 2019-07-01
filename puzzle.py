import random
random.seed(10)

puzzle = [  0,
           1,1,
          1,1,1,
         1,1,1,1,
        1,1,1,1,1]

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
    puzzle[t[0]] = 0
    puzzle[t[1]] = 1

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