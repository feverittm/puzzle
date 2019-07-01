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
def valid_moves():
    # first set should be [(3,0),(5,0)]
    del valid[::]
    t= tuple()
    for x in range(15):
        # up-right move
        if x<11:
            if puzzle[x+3] == 1 and puzzle[x] == 0:
                t = x+3,x
                valid.append(t)
        # up-left move
        if x<9:
            if puzzle[x+5] == 1 and puzzle[x] == 0:
                t = x+5,x
                valid.append(t)
    return valid

"""
choose which move we want to use for this round
"""
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
    puzzle[move[0]] = 0
    puzzle[move[1]] = 1
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